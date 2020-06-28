
import math
import heimdall.codescan.plugins.scan as scan

class ShannonEntropy(scan.IScan):

    BASE64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

    def scan(self, text):
        return self.shannon_entropy(text)

    def shannon_entropy(self, data):
        _entropy = 0
        _data_length = len(data)
        for character_i in ShannonEntropy.BASE64_CHARS:
            _px = data.count(character_i) / _data_length
            if _px > 0:
                _entropy += - _px * math.log(_px, 2)
        return _entropy
