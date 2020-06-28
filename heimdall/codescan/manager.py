#!usr/bin/env python


"""Manager of codescan process.

This module is for scanning the code via different plugins available to this
module.
"""

import fileinput
import getpass
import os
import os.path as path
import shutil
import subprocess
import sys
from io import StringIO

from heimdall import config
from heimdall.codescan.plugins import manager


class CodescanManager:

    def __init__(self):
        self.plugin_manager = manager.CodescanPluginManager()

    def init(self):
        _config_path = config.get_config_path()
        _path = os.path.expanduser('~/.gitconfig')
        _hook_template_config_path = '\ttemplatedir = %s' % \
            os.path.join(_config_path, 'res/heimdall')

        val = False
        for line in fileinput.input(_path, inplace=True):
            if 'templatedir' in line.strip():
                val = True
                line = line.replace(line, _hook_template_config_path)
            sys.stdout.write(line)
        if val:
            return
        _hook_template_config_path = '\n[init]\n %s' % \
            _hook_template_config_path
        _git_config_file_append_mode = open(_path, 'a+')
        _git_config_file_append_mode.write(_hook_template_config_path)
        _git_config_file_append_mode.close()

    def scan(self, argv):
        if len(argv) > 1:
            _repo_abs_dir_path = argv[0]
            _files = []
            _file_name_list = argv[1].split()
            _result_list = self.plugin_manager.scan(_repo_abs_dir_path, _file_name_list)
            _result = self.format_data(_result_list)
            return _result


    def format_data(self, result_list):
        _final_result = StringIO()
        if result_list:
            for item_map in result_list:
                reason_dict = item_map['reason']
                for reason_key in reason_dict:
                    _val_list = reason_dict[reason_key]
                    for item in _val_list:
                        _val = '\x1b[91mReason : ' + reason_key + '\x1b[0m\n'
                        _final_result.write(_val)
                        _final_result.write('\x1b[91mFile name : '+item_map['file'] + '\x1b[0m\n')
                        _final_result.write('\x1b[93mFound : '+item+'\x1b[0m\n')
                        _final_result.write('\n\n')
        return _final_result.getvalue().strip()


    def register(self, argv):
        if argv:
            for repo_path in argv:
                if path.exists(repo_path):
                    _repo_root_path = config.get_git_repo_path(repo_path)
                    _repo_git_hook_path = path.join(_repo_root_path,'.git/hooks')
                    _current_dir = config.get_config_path()
                    _res_dir = path.join(_current_dir,'res/heimdall/hooks')
                    _res_hook_files = os.listdir(_res_dir)
                    for file in _res_hook_files:
                        _file_name = path.join(_res_dir, file)
                        if path.isfile(_file_name):
                            _dest_file = path.join(_repo_git_hook_path, file)
                            shutil.copyfile(_file_name, _dest_file)
                            _relative_dest_file = path.join('.git/hooks', file)
                            p = subprocess.run(["chmod", "a+x", _relative_dest_file], cwd=_repo_root_path, capture_output=False, shell=False)


    def unregister(self, argv):
        if argv:
            for repo_path in argv:
                if path.exists(repo_path):
                    _repo_root_path = config.get_git_repo_path(repo_path)
                    _current_dir = config.get_config_path()
                    _res_dir = path.join(_current_dir,'res/heimdall/hooks')
                    _res_hook_files = os.listdir(_res_dir)
                    for file in _res_hook_files:
                        _file_name = path.join(_res_dir, file)
                        if path.isfile(_file_name):
                            _relative_dest_file = path.join('.git/hooks', file)
                            #print(_relative_dest_file)
                            _abs_path = path.join(_repo_root_path, _relative_dest_file)
                            if path.exists(_abs_path):
                                p = subprocess.run(["rm", _relative_dest_file], cwd=_repo_root_path, capture_output=False, shell=False)
