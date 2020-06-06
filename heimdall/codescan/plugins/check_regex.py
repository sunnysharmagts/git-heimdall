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
            self.regexes.append(re.compile(regexes[key], re.MULTILINE))

    def scan(self, text):
        _results = []
        for regex in self.regexes:
            for m in re.finditer(regex, text):
                start = m.start()
                lineno = text.count('\n', 0, start) + 1
                offset = start - text.rfind('\n', 0, start)
                word = m.group()
                _results.append(word)
                #print("(%s,%s): %s" % (lineno, offset, word))
        return _results
