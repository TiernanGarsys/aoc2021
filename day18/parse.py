from collections import namedtuple

Test = namedtuple('Test', ['header', 'numbers'])

def parse_file(filename: str) -> list[Test]:  
    test_strings = []
    contents = ''
    with open(filename) as file:
        test_strings = file.read().split('-')

    tests = []
    for test_string in test_strings:
        header = 'NO HEADER'
        numbers = []
        lines = test_string.splitlines()
        for line in lines:
            if not len(line):
                continue
            if '=' in line:
                header = line.strip()
            else:
                numbers.append(line.strip())
        tests.append(Test(header=header, numbers=numbers))
    
    return tests

