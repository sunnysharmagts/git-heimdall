#!usr/bin/env python


"""Manager of codescan plugins.

This module is for scanning the code via different plugins available to this
module.
"""

from heimdall.codescan.plugins import secrets_checker
from heimdall.codescan.plugins import base64_entropy
from heimdall.codescan.plugins import check_regex

import os


class CodescanPluginManager:

    def __init__(self):
        self.plugins = []
        self.plugins.append(base64_entropy.Base64Entropy())
        self.plugins.append(check_regex.RegexCheck())

    def scan(self, repo_path, files):
        result = []
        for file_name in files:
            _full_file_name = os.path.join(repo_path, file_name)
            file = open(_full_file_name, "r")
            text = file.read()
            for plugin in self.plugins:
                _result_map = plugin.scan(text)
                if _result_map is not None and len(_result_map) > 0:
                    _final_map = dict()
                    _final_map['reason'] = _result_map
                    _final_map['file'] = file_name
                    result.append(_final_map)
            file.close()
        return result
