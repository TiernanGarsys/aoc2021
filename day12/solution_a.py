# Advent of Code 2021, Day 12, Solution A

import sys

from collections import defaultdict
from functools import reduce

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file')

    filename = sys.argv[1]
  
    graph = defaultdict(list)
    with open(filename) as file:
        for l in file.readlines():
            tokens = l.split('-')
            graph[tokens[0].strip()].append(tokens[1].strip())
            graph[tokens[1].strip()].append(tokens[0].strip())

    paths = search(graph, ['start'])  
    print('The answer is %i' % len(paths))


def search(graph, seen):
    curr = seen[-1]

    if curr == 'end':
        return [seen]

    searchable_neighbors = [n for n in graph[curr] if n.isupper() or n not in seen]
    return [p for n in searchable_neighbors for p in search(graph, seen + [n])]

if __name__ == '__main__':
    run()
