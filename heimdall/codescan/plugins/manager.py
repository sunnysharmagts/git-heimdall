#!usr/bin/env python


"""Manager of codescan plugins.

This module is for scanning the code via different plugins available to this module.
"""

from heimdall.codescan.plugins import secrets_checker

class CodescanPluginManager:

    def __init__(self):
        self.plugins = []
        self.plugins.append(secrets_checker.SecretsChecker())

    def scan(self, files):
        #for plugin in self.plugins:
        _val = self.plugins[0].scan(files)
        return _val
