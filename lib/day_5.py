import hashlib
import re

class PasswordFinder(object):
    def run_simple_mode(self, door_id):
        password = ''
        counter = 0
        while len(password) < 8:
            data = door_id + str(counter)
            code = hashlib.md5(data.encode('utf-8')).hexdigest()
            if code[0:5] == '00000':
                password += code[5]
            counter += 1
        return password

    def run_advanced_mode(self, door_id):
        password = list('????????')
        counter = 0
        while '?' in password:
            data = door_id + str(counter)
            code = hashlib.md5(data.encode('utf-8')).hexdigest()
            if code[0:5] == '00000' and re.search('[0-7]', code[5]):
                index = int(code[5])
                if password[index] == '?':
                    del password[index]
                    password.insert(index, code[6])
            counter += 1
        return ''.join(password)
