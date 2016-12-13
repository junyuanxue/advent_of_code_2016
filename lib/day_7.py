import re

class IPChecker(object):
    def count(self, ips, tech):
        ips = ips.strip().split('\n')
        tally = 0
        for ip in ips:
            criteria = self._supports_tls(ip) if tech == 'tls' else self._supports_ssl(ip)
            if criteria:
                tally += 1
        return tally

    def _get_supernet_strings(self, ip):
        return re.findall(r'\]\w+$|^\w+\[|\]\w+\[', ip)

    def _get_hypernet_strings(self, ip):
        return re.findall(r'\[\w+\]', ip)

    def _supports_tls(self, ip):
        supernet_strings = self._get_supernet_strings(ip)
        hypernet_strings = self._get_hypernet_strings(ip)
        return self._has_abba(supernet_strings) and not self._has_abba(hypernet_strings)

    def _has_abba(self, strings):
        for string in strings:
            i = 0
            while i <= len(string) - 4:
                if string[i] != string[i + 1] and string[i + 1] == string[i + 2] and string[i + 2] != string[i + 3] and string[i] == string[i + 3]:
                    return True
                else:
                    i += 1
        return False

    def _supports_ssl(self, ip):
        supernet_strings = self._get_supernet_strings(ip)
        hypernet_strings = self._get_hypernet_strings(ip)
        aba = self._has_aba(supernet_strings)
        bab = aba[1] + aba[0] + aba[1]
        return aba and self._has_bab(hypernet_strings, bab)

    def _has_aba(self, strings):
        for string in strings:
            i = 0
            while i <= len(string) - 3:
                if string[i] != string[i + 1] and string[i] == string[i + 2]:
                    return string[i] + string[i + 1] + string[i]
                else:
                    i += 1
        return False

    def _has_bab(self, strings, bab):
        for string in strings:
            if bab in string:
                return True
        return False
