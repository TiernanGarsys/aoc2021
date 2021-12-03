# Advent of Code 2021, Day 3, Solution B

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

    def oxygen_test(reading_bit, modal_bit):
        return (modal_bit is not None and reading_bit == modal_bit) or (modal_bit is None and reading_bit == 1)

    def carbon_test(reading_bit, modal_bit):
        return (modal_bit is not None and reading_bit != modal_bit) or (modal_bit is None and reading_bit == 0)

    oxygen_reading = filter_readings(readings, oxygen_test)
    carbon_reading = filter_readings(readings, carbon_test)

    print('The answer is %i' % (int(oxygen_reading, 2) * int(carbon_reading, 2)))


def filter_readings(readings: list[str], fxn) -> Optional[str]:
    filtered_readings = readings[:]
    for i in range(0, len(readings[0])):
        if len(filtered_readings) <= 1:
            break

        distribution: defaultdict[int, dict[int, int]] = defaultdict(dict)
        for reading in filtered_readings:
            for j, bit in enumerate(reading):
                int_bit = int(bit)
                distribution[j][int_bit] = distribution[j].get(int_bit, 0) + 1

        modal_bits: dict[int, Optional[int]] = dict()

        for j in range(0, len(distribution)):
            subdistribution = distribution[j]
            if subdistribution.get(0, 0) > subdistribution.get(1, 0):
                modal_bits[j] = 0 
            elif subdistribution.get(0, 0) < subdistribution.get(1, 0):
                modal_bits[j] = 1 
            else:
                modal_bits[j] = None
    
        filtered_readings = list(filter(lambda r: fxn(int(r[i]), modal_bits[i]), filtered_readings))

    return filtered_readings[0]
   

if __name__ == '__main__':
    run()
