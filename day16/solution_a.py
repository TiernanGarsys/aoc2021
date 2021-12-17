# Advent of Code 2021, Day 16, Solution A

import sys

from dataclasses import dataclass
from functools import reduce
from typing import Optional

@dataclass
class Packet():
    tid: int
    version: int
    lid: Optional[int]
    value: Optional[int]
    children: list

    def version_sum(self):
        return self.version + sum([c.version_sum() for c in self.children])

    def evaluate(self):
        if self.tid == 0:
            return sum([c.evaluate() for c in self.children])
        elif self.tid == 1:
            return reduce(lambda a, c: a * c.evaluate(), self.children, 1)
        elif self.tid == 2:
            return sorted([c.evaluate() for c in self.children])[0]
        elif self.tid == 3:
            return sorted([c.evaluate() for c in self.children])[-1]
        elif self.tid == 4:
            return self.value
        elif self.tid == 5:
            return 1 if self.children[0].evaluate() > self.children[1].evaluate() else 0
        elif self.tid == 6:
            return 1 if self.children[0].evaluate() < self.children[1].evaluate() else 0
        elif self.tid == 7:
            return 1 if self.children[0].evaluate() == self.children[1].evaluate() else 0
        else:
            raise ValueError('Invalid Type ID for packet: %s' % self.tid)

hex_to_binary = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file ')

    filenames = sys.argv[1:]

    for filename in filenames:
        run_file(filename)

def run_file(filename):
    contents = ''
    with open(filename) as file:
        contents = file.read().strip()
    message = ''.join([hex_to_binary[c] for c in contents])

    packet, excess = parse_message(message)
    print('The version sum is %i' % packet.version_sum())
    print('The evaluated value is %i' % packet.evaluate())

def parse_message(message) -> (Packet, str):
    if len(message) < 6:
        return None, message

    version, tid, rest = int(message[0:3], 2), int(message[3:6], 2), message[6:]

    if tid == 4:
        bitstring = ''
        while True:
            is_last, chunk, rest = int(rest[0], 2), rest[1:5], rest[5:]
            bitstring += chunk
            if is_last == 0:
                value = int(bitstring, 2)
                return Packet(tid=tid, version=version, lid=None, value=value, children=[]), rest
    else:
        lid, rest = int(rest[0], 2), rest[1:]
        children = []
        if lid == 0:
            children_bitwidth, rest = int(rest[:15], 2), rest[15:]
            final_bitwidth = len(rest) - children_bitwidth
            while len(rest) and len(rest) > final_bitwidth:
                child_packet, rest = parse_message(rest)
                children.append(child_packet)
        elif lid == 1:
            children_num, rest = int(rest[:11], 2), rest[11:]
            for _ in range(children_num):
                child_packet, rest = parse_message(rest)
                children.append(child_packet)

        return Packet(tid=tid, version=version, lid=lid, value=None, children=children), rest


if __name__ == '__main__':
    run()
