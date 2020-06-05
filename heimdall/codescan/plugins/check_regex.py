import re
import json
import os
import heimdall.codescan.plugins.scan as scan
from heimdall import config

class RegexCheck(scan.IScan):

    def __init__(self):
        _config_path = config.get_config_path()
        self.regexes = []
        with open(os.path.join(os.path.dirname(_config_path), "heimdall/res/regex.json"), 'r') as f:
            regexes = json.loads(f.read())

        for key in regexes:
            self.regexes.append(re.compile(regexes[key]))

    def scan(self, word):
        for regex in self.regexes:
            _match = regex.findall(word)
            if _match:
                return _match
