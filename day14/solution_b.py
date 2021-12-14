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
                a, b, c = tokens[0][0], tokens[0][1], tokens[2][0]
                rules[a + b] = [a + c, c + b]
            elif len(line.strip()):
                template = [c for c in line.strip()]


    pairs = defaultdict(int)
    for idx in range(len(template) - 1):
        a, b = template[idx], template[idx+1]
        pairs[a + b] += 1

    for n in range(iterations):
        new_pairs = defaultdict(int)
        for k, v in pairs.items():
            outputs = rules.get(k)
            if outputs:
                for o in outputs:
                   new_pairs[o] += v

        pairs = new_pairs

    # To avoid double-counting letters from the distribution, we only count the instances of the 
    # suffix of each pair. We then increase the count of the lead character in the template
    # by one, since it won't be the suffix of any pair.
    count = defaultdict(int)
    for k, v in pairs.items():
        a, b = k
        count[b] += v
    count[template[0]] += 1

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
