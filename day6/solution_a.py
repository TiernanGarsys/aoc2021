# Advent of Code 2021, Day 6, Solution A

import sys

from dataclasses import dataclass

@dataclass
class Fishy():
    timer: int 

    def pass_time(self) -> bool:
        if self.timer == 0:
            self.timer = 6
            return True
        else:
            self.timer = self.timer - 1
            return False

def run():
    if len(sys.argv) < 3:
        raise ValueError('No arguments provided. Usage: solution.py input_file days')

    filename = sys.argv[1]
    days_to_simulate = int(sys.argv[2])
   
    fishies = []
    with open(filename) as file:
        fishies = [Fishy(timer=int(f)) for f in file.read().split(',')]

    for _ in range(days_to_simulate):
        fishies_to_spawn = 0
        for f in fishies:
            reset = f.pass_time()
            if reset:
                fishies_to_spawn += 1

        for _ in range(fishies_to_spawn):
            fishies.append(Fishy(timer=8))

    print('The answer is %i' % len(fishies))

if __name__ == '__main__':
    run()
