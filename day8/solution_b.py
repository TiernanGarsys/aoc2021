# Advent of Code 2023, Day 8, Solution B

import functools
import sys

from collections import defaultdict

signal_to_digit = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9',
}

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file days')

    filename = sys.argv[1]

    tests = []
    with open(filename) as file:
        for line in file.readlines():
            note = line.split('|')
            tests.append((note[0].split(), note[1].split()))

    total = 0
    for signals, display in tests:
        mapping = get_mapping_for_signals(signals)
        total += get_reading_for_display(mapping, display)

    print('The answer is %s' % total)


def get_reading_for_display(mapping, display):
    digits = ''

    for unmapped_signal in display:
        mapped_signal = ''
        for c in unmapped_signal:
            mapped_signal += mapping[c]

        digits += signal_to_digit[''.join(sorted(mapped_signal))]

    return int(digits)

def get_mapping_for_signals(signals):
    two_seg = None
    three_seg = None
    four_seg = None
    seven_seg = None
    segment_to_frequency = defaultdict(int)

    for signal in signals:
        if len(signal) == 2:
            two_seg = signal
        elif len(signal) == 3:
            three_seg = signal
        elif len(signal) == 4:
            four_seg = signal
        elif len(signal) == 7:
            seven_seg = signal

        for segment in signal:
            segment_to_frequency[segment] += 1

    mapping = dict()

    # The segment that appears in the 7 but not in 1 is A
    mapping['a'] = [c for c in three_seg if c not in two_seg][0]

    # The segment that is used 6 times is B
    mapping['b'] = [k for k, v in segment_to_frequency.items() if v == 6][0]
    # The segment that is used 4 times is E
    mapping['e'] = [k for k, v in segment_to_frequency.items() if v == 4][0]
    # The segment that is used 9 times is F
    mapping['f'] = [k for k, v in segment_to_frequency.items() if v == 9][0]

    ### The segment that is used 7 times, but not in 4, is G
    mapping['g'] = [k for k, v in segment_to_frequency.items() if v == 7 and k not in four_seg][0]

    # The segment that is used 8 times and is not A is C
    mapping['c'] = [k for k, v in segment_to_frequency.items() if v == 8 and k is not mapping['a']][0]

    ### The segment that is unmapped is D
    mapping['d'] = [k for k, v in segment_to_frequency.items() if k not in mapping.values()][0]

    # Silly me didn't realize the inverse mapping is what I actually needed 
    return {v: k for k, v in mapping.items()}

if __name__ == '__main__':
    run()
