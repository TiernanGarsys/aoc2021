# Advent of Code 2021, Day 20, Solution

import sys

from collections import namedtuple

Bounds = namedtuple('Bounds', ['lr', 'lc', 'hr', 'hc'])
Pixel = namedtuple('Pixel', ['r', 'c'])

def run():
    if len(sys.argv) < 3:
        raise ValueError('No arguments provided. Usage: solution.py input_file iterations')

    filename = sys.argv[1]
    iterations = int(sys.argv[2])
    image, algorithm = parse_input(filename) 
    infinity_pixel = '.'
  
    for n in range(iterations):
        bounds = get_bounds(image)

        enhanced_image = set()
        for r in range(bounds.lr-1, bounds.hr+2):
            for c in range(bounds.lc-1, bounds.hc+2):
                bitstring = ''

                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        is_infinity = out_of_bounds(bounds, i, j) and infinity_pixel == '#'
                        is_one = Pixel(r=i, c=j) in image or is_infinity
                        bitstring = bitstring + ('1' if is_one else '0')

                idx = int(bitstring, 2)
                if algorithm[idx] == '#':
                    enhanced_image.add(Pixel(r=r, c=c))

        image = enhanced_image
        infinity_pixel = algorithm[-1] if infinity_pixel == '#' else algorithm[0]

    print('The answer is %s' % len(image))


def out_of_bounds(bounds, r, c):
    return r < bounds.lr or r > bounds.hr or c < bounds.lc or c > bounds.hc


def get_bounds(image):
    max_r = max_c = -sys.maxsize
    min_r = min_c = sys.maxsize

    for p in image:
        if p.r > max_r:
            max_r = p.r
        if p.c > max_c: 
            max_c = p.c
        if p.r < min_r: 
            min_r = p.r
        if p.c < min_c:
            min_c = p.c

    return Bounds(lr=min_r, lc=min_c, hr=max_r, hc=max_c)


def parse_input(filename):
    algorithm = ''
    raw_image = []

    with open(filename) as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            if not algorithm:
                algorithm = line
            elif line: 
                raw_image.append(line)
    
    image = set()
    for i in range(len(raw_image)):
        for j in range(len(raw_image[i])):
            if raw_image[i][j] == '#':
                image.add(Pixel(r=i, c=j))

    return image, algorithm

if __name__ == '__main__':
    run()

