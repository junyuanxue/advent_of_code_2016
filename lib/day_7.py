import re

class IPChecker(object):
    def count(self, ips):
        ips = ips.strip().split('\n')
        tally = 0
        for ip in ips:
            if self._supports_tls(ip):
                tally += 1
        return tally

    def _supports_tls(self, ip):
        normal_strings = re.findall(r'\]\w+$|^\w+\[|\]\w+\[', ip)
        hypernet_strings = re.findall(r'\[\w+\]', ip)
        return self._has_abba(normal_strings) and not self._has_abba(hypernet_strings)

    def _has_abba(self, strings):
        for string in strings:
            string = re.sub(r'[^a-zA-Z]+', '', string)
            i = 0
            while i <= len(string) - 4:
                if string[i] != string[i + 1] and string[i + 1] == string[i + 2] and string[i + 2] != string[i + 3] and string[i] == string[i + 3]:
                    return True
                else:
                    i += 1
