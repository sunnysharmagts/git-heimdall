
import heimdall.codescan.plugins.scan as scan
import math

class ShannonEntropy(scan.IScan):

    def scan(self, word):
        return self.shannon_entropy(word)

    def shannon_entropy(self, data):
        _entropy = 0
        BASE64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
        _data_length = len(data)
        for character_i in BASE64_CHARS:
            _px = data.count(character_i) / _data_length
            if _px > 0:
                _entropy += - _px * math.log(_px, 2)
        return _entropy
