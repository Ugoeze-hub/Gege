from os import strerror
class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # Write your code here.
        def __init__(self, line_number, line_string, error_message = 'Invalid Line'):
            super().__init__(self)
            self.line_number = line_number
            self.line_string = line_string
            

class FileEmpty(StudentsDataException):
    # Write your code here.
        def __init__(self, error_message = 'File does not exist'):
            super().__init__(self)

FileName = input('Enter a file name: ') 
print('Record sheet', sep = '\n')

data = {}

try:
    with open(FileName, 'rt') as Read_File_Sample:
        read_file = Read_File_Sample.readlines()
        if len(read_file) == 0:
            raise FileEmpty
        for i in range(len(read_file)):
            lines = read_file[i]
            words = lines.split()
            if len(words) != 3:
                raise BadLine(f'Line # {i + 1}', lines)
            student = words[0] + ' ' + words[1]
            score = words[2]
            try:
                score = float(score)
            except ValueError:
                raise BadLine('Line #' + (i + 1), lines)
            try:
                data[student] += score
            except KeyError:
                data[student] = score

        for student in sorted(data.keys()):
            print(student, '   ', data[student])

except IOError as e:
    print('I/O Error occured: ', strerror(e.errno))
except BadLine as e:
    print('BadLine #' + str(e.line_number) + ' in source file' + e.line_string)
except FileEmpty as e:
    print('Source File Empty')