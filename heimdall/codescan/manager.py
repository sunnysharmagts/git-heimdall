#!usr/bin/env python


"""Manager of codescan process.

This module is for scanning the code via different plugins available to this module.
"""

import fileinput
import os
import sys

from heimdall import config
from heimdall.codescan.plugins import manager


class CodescanManager:

    def __init__(self):
        self.plugin_manager = manager.CodescanPluginManager()

    def init(self):
        _config_path = config.get_config_path()
        _path = os.path.expanduser('~/.gitconfig')
        _hook_template_config_path = '\ttemplatedir = %s' % os.path.join(_config_path, 'res/heimdall')

        val = False
        for line in fileinput.input(_path, inplace=True):
            if 'templatedir' in line.strip():
                val = True
                line = line.replace(line, _hook_template_config_path)
            sys.stdout.write(line)
        if val:
            return
        _hook_template_config_path = '\n[init]\n %s' % _hook_template_config_path
        _git_config_file_append_mode = open(_path, 'a+')
        _git_config_file_append_mode.write(_hook_template_config_path)
        _git_config_file_append_mode.close()

    def scan(self, argv):
        if len(argv) > 1:
            _repo_abs_dir_path = argv[0]
            _files = []
            _file_name_list = argv[1].split()
            for file in _file_name_list:
                _files.append(os.path.join(_repo_abs_dir_path, file))
            self.plugin_manager.scan(_files)
