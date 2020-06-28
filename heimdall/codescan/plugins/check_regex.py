import re
import json
import os
import heimdall.codescan.plugins.scan as scan
import heimdall.codescan.plugins.entropy as entropy
from heimdall import config

class RegexCheck(scan.IScan):

    HEX_THRESHOLD = 2.7

    def __init__(self):
        _config_path = config.get_config_path()
        self.regexes = dict()
        self.entropy = entropy.ShannonEntropy()
        with open(os.path.join(os.path.dirname(_config_path), "heimdall/res/regex.json"), 'r') as f:
            regexes = json.loads(f.read())

        for key in regexes:
            self.regexes[key] = re.compile(regexes[key], re.MULTILINE)

    def scan(self, text):
        _results_map = dict()
        for key in self.regexes:
            for m in re.finditer(self.regexes[key], text):
                start = m.start()
                lineno = text.count('\n', 0, start) + 1
                offset = start - text.rfind('\n', 0, start)
                word = m.group()
                _score = self.entropy.scan(word)
                if _score > RegexCheck.HEX_THRESHOLD:
                    if key not in _results_map:
                        _val = []
                    _val.append(word)
                    _results_map[key] = _val
        return _results_map
