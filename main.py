from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

PRIVATE_VARIABLE_ERROR_IDENTIFIER = ' is private and only accessible within class '
PROJECT_ROOT = 'PATH_TO_YOUR_PROJECT'

def read_log_file(file_name = 'log.txt'):
    return list(map(lambda line : line.strip(), open(file_name).readlines()))

def is_usage_of_private_variable_error(line):
    return PRIVATE_VARIABLE_ERROR_IDENTIFIER in line

def parse_line(line):
    line = line.split(': :')
    file_name = line[0].split('.html(')[0] + '.ts'
    return {
        'file_name': file_name,
        'variable_name': line[1].split('\'')[1],
        'class': line[1].split('\'')[3]
    }

def fix_error(fix):
    found_class = False
    fh, abs_path = mkstemp()
    file_path = PROJECT_ROOT + fix['file_name']
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for l in old_file.readlines():
                if 'class ' + fix['class'] in l:
                    found_class = True
                if found_class and 'private ' + fix['variable_name'] in l:
                    l = l.replace('private ' + fix['variable_name'], 'public ' + fix['variable_name'])
                new_file.write(l)
    remove(file_path)

    move(abs_path, file_path)

def main():
    lines = filter(is_usage_of_private_variable_error, read_log_file())
    fixes = map(parse_line, lines)

    for fix in fixes:
        fix_error(fix)


if __name__ == '__main__':
    main()
