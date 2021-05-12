import os.path
class File:
    def __init__(self, file_name):
        self.file_name = file_name
        f = open(self.file_name, 'w')
        f.close()
        self._length = 0
        self._current = 0
        self._all_strings_file = None


    def __add__(self, obj):
        sting_f1 = self.read()
        sting_f2 = obj.read()
        new_file = File('new_file')
        new_file.write(sting_f1+sting_f2)

        return new_file

    def __iter__(self):
        return self

    def __next__(self):

        if self._all_strings_file == None:
            self._all_strings_file = []
            with open(self.file_name) as f:
                while True:
                    line = f.readline()

                    if len(line) == 0:
                        break
                    self._all_strings_file.append(line)
            self._length = len(self._all_strings_file)

        if self._current >= self._length:
            raise StopIteration

        result = self._all_strings_file[self._current]
        self._current += 1

        return result

    def read(self):
        with open(self.file_name, 'r') as f:
            return f.read()

    def write(self, string):
        with open(self.file_name, 'w') as f:
            f.write(string)

    def __str__(self):
        return os.path.abspath(self.file_name)

def test():
    path_to_file = 'some_filename'

    print('5 {} have to return False'.format(os.path.exists(path_to_file)))

    file_obj = File(path_to_file)
    print('8 {} -- have to return True'.format(os.path.exists(path_to_file)))
    print('10 {} -- have to retrun Empty string'.format(file_obj.read()))

    file_obj.write('some text')
    print('13 {} -- have to retrun \'some text\''.format(file_obj.read()))

    file_obj.write('other text')

    print('18 {} -- have to return \'other text\''.format(file_obj.read()))
    file_obj_1 = File(path_to_file + '_1')
    file_obj_2 = File(path_to_file + '_2')
    file_obj_1.write('line 1\n')
    file_obj_2.write('line 2\n')
    new_file_obj = file_obj_1 + file_obj_2
    print('26 {} -- have to return True'.format(isinstance(new_file_obj, File)))

    print('29 {} -- have to return path new file'.format(new_file_obj))
    for line in new_file_obj:
        print(ascii(line))

if __name__ == "__main__":
    test()











