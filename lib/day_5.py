import hashlib

class PasswordFinder(object):
    def run(self, door_id):
        password = ''
        index = 0
        while len(password) < len(door_id):
            data = door_id + str(index)
            code = hashlib.md5(data.encode('utf-8')).hexdigest()
            print(code)
            if (code[0:3] == '00000'):
                password += code[5]
            index += 1
        return password
