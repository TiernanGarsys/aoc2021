# Advent of Code 2021, Day 14, Solution A

import sys

from collections import defaultdict

def run():
    if len(sys.argv) < 3:
        raise ValueError('No arguments provided. Usage: solution.py input_file iterations')

    filename = sys.argv[1]
    iterations = int(sys.argv[2])

    template = None
    rules = dict()

    with open(filename) as file:
        for line in file.readlines():
            if '->' in line:
                tokens = line.split()
                rules[tokens[0].strip()] = tokens[2].strip()
            elif len(line.strip()):
                template = [c for c in line.strip()]

   
    polymer = template

    for n in range(iterations):
        next_polymer = []
        for idx in range(len(polymer)):
            elt1 = polymer[idx]
            next_polymer.append(elt1)

            if idx == len(polymer) - 1:
                continue
           
            elt2 = polymer[idx+1]

            inserted = rules.get(elt1 + elt2)

            if inserted:
                next_polymer.append(inserted)

        polymer = next_polymer

    count = defaultdict(int)
    for e in polymer:
        count[e] += 1

    common_elt, common_val, rare_elt, rare_val = '', 0, '', sys.maxsize

    for k, v in count.items():
        if v > common_val:
            common_elt = k
            common_val = v
        elif v < rare_val:
            rare_elt = k
            rare_val = v

    print('The answer is %i' % (common_val - rare_val))



if __name__ == '__main__':
    run()
