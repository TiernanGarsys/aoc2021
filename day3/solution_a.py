# Advent of Code 2021, Day 3, Solution A

import sys

from collections import defaultdict
from typing import Optional

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file')

    filename = sys.argv[1]
   
    readings = []
    with open(filename) as file:
        readings = [r.strip() for r in file.readlines()]

    distribution: defaultdict[dict[str, int]] = defaultdict(dict)
   
    bit_width = 0
    for reading in readings:
        bit_width = max(bit_width, len(reading))

        for idx, bit in enumerate(reading):
            int_bit = int(bit)
            distribution[idx][int_bit] = distribution[idx].get(int_bit, 0) + 1

    gamma_reading = ''
    for idx in range(0, bit_width):
        gamma_reading += str(get_highest_valued_key(distribution[idx]))

    epsilon_reading = ''.join(['0' if x == '1' else '1' for x in gamma_reading])

    print('The answer is %i' % (int(gamma_reading, 2) * int(epsilon_reading, 2)))


def get_highest_valued_key(distribution: dict[str, int]) -> Optional[str]:
    max_key = None
    max_val = 0

    for key, val in distribution.items():
        if val > max_val:
            max_key = key
            max_val = val

    return max_key
    
if __name__ == '__main__':
    run()
