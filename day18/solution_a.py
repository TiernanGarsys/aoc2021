# Advent of Code 2021, Day 18, Solution A

import parse
import math
import sys


def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file ')

    filename = sys.argv[1]
    tests = parse.parse_file(filename)
    for test in tests:
        run_test(test)


def run_test(test: parse.Test):
    print('Running test: %s' % test.header)

    summation = test.numbers[0]
    for number in test.numbers[1:]: 
        summation = '[%s,%s]' % (summation, number)
        while True:
            summation, modified = explode(summation)
            if modified:
                continue

            summation, modified = split(summation)
            if modified:
                continue
            else:
                break

    answer = magnitude(summation)

    print('Summation: %s' % summation)
    print('Answer: %s' % answer)


def explode(summation):
    tokens = tokenize(summation)
    open_braces = 0
    close_braces = 0

    for i in range(len(tokens) - 2):
        t0, t1, t2 = tokens[i], tokens[i+1], tokens[i+2]
        if t0.isnumeric() and t1 == ',' and t2.isnumeric() and open_braces >= close_braces + 5:
            for j in range(i-1, 0, -1):
                if tokens[j].isnumeric():
                    tokens[j] = str(int(tokens[j]) + int(t0))
                    break
            for j in range(i+3, len(tokens)):
                if tokens[j].isnumeric():
                    tokens[j] = str(int(tokens[j]) + int(t2))
                    break

            return ''.join(tokens[:i-1] + ['0'] + tokens[i+4:]) , True

        elif t0 == '[':
            open_braces += 1
        elif t0 == ']':
            close_braces += 1

    return summation, False

def split(summation):
    tokens = tokenize(summation)
    for i in range(len(tokens)):
        t0 = tokens[i] 
        if t0.isnumeric() and int(t0) >= 10:
            left, right = str(math.floor(int(t0) / 2)), str(math.ceil(int(t0) / 2))
            return ''.join(tokens[:i] + ['[', left, ',', right, ']'] + tokens[i+1:]) , True

    return summation, False


def magnitude(summation):
    if summation.isnumeric():
        return int(summation)

    open_brackets = 0
    close_brackets = 0

    tokens = tokenize(summation)
    for idx, t in enumerate(tokens):
        if t == '[':
            open_brackets += 1
        elif t == ']':
            close_brackets += 1
        elif t == ',' and open_brackets == close_brackets + 1:
            ln = ''.join(tokens[1:idx])
            rn = ''.join(tokens[idx+1:-1])
            return 3 * magnitude(ln) + 2 * magnitude(rn)

def tokenize(summation):
    tokens = []
    i = 0
    while i < len(summation):
        if summation[i] == '[' or summation[i] == ']' or summation[i] == ',':
            token = summation[i]
            i += 1
        else:
            token = ''
            while summation[i].isnumeric():
               token += summation[i] 
               i += 1

        tokens.append(token)

    return tokens

if __name__ == '__main__':
    run()

