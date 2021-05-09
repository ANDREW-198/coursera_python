import os.path
class File:
    def __init__(self, file_name):
        self.file_name = file_name
        f = open(self.file_name, 'w')
        f.close()

    def __add__(self, obj):
        with open(self.file_name, 'r') as f:
            sting_f1 = f.read()
        with open(obj.file_name, 'r') as f:
            sting_f2 = f.read()
        with open('new_file', 'w') as f:
            print('добавляют к строке {} строку {} и получаю {}'.format(sting_f1, sting_f2,sting_f1+sting_f2))
            f.write(sting_f1+sting_f2)

    def read(self):
        with open(self.file_name, 'r') as f:
            return f.read()

    def write(self, string):
        with open(self.file_name, 'w') as f:
            f.write(string)

    def __str__(self):
        return os.path.abspath(self.file_name)

