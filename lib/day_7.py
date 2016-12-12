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

        normal_strings = []
        hypernet_strings = re.findall(r'\[\w+\]', ip)
        # while '[' in ip or ']' in ip:
        #     normal_strings.append(ip.split('[')[0])
        #     ip = ip.split('[')[1]
        #     hypernet_strings.append(ip.split(']')[0])
        #     ip = ip.split(']')[1]
        print(normal_strings)
        print(hypernet_strings)
        return self._has_abba(normal_strings) and not self._has_abba(hypernet_strings)

    def _has_abba(self, strings):
        for string in strings:
            print(string)
