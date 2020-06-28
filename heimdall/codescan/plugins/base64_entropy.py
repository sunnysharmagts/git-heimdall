

import heimdall.codescan.plugins.scan as scan
import heimdall.codescan.plugins.entropy as entropy
import math

class Base64Entropy(scan.IScan):

    BASE_64_THRESHOLD = 4.5
    HIGH_ENTROPY = 'High Entropy'

    def __init__(self):
        self.entropy = entropy.ShannonEntropy()


    def scan(self, text):
        return self.check_entropy(text)

    def check_entropy(self, text):
        _lines = text.split('\n')
        _high_entropy_map = dict()
        for line in _lines:
            _words = line.split()
            for word in _words:
                _score = self.entropy.scan(word)
                if _score > Base64Entropy.BASE_64_THRESHOLD:
                    _val = None
                    if Base64Entropy.HIGH_ENTROPY not in _high_entropy_map:
                        _val = []
                    else:
                        _val = _high_entropy_map[Base64Entropy.HIGH_ENTROPY]
                    _val.append(word)
                    _high_entropy_map[Base64Entropy.HIGH_ENTROPY] = _val
        return _high_entropy_map
