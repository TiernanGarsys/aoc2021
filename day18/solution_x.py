# Advent of Code 2021, Day 18, Solution A

import parse
import sys

from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class Node():
    parent: Any
    # Children
    lc: Any
    rc: Any
    # Values
    rv: Optional[int]
    lv: Optional[int]

    def traversal(self):
        lt = self.lc.traversal() if self.lc else []
        rt = self.rc.traversal() if self.rc else []
        return lt + [self] + rt

def run():
    if len(sys.argv) < 2:
        raise ValueError('No arguments provided. Usage: solution.py input_file ')

    filename = sys.argv[1]
    tests = parse.parse_file(filename)
    for test in tests:
        run_test(test)


def run_test(test: parse.Test):
    print('Running test: %s' % test.header)

    tree = None
    for number in test.numbers: 
        if tree:
            tree = add(tree, number)
        else:
            tree = build_tree(number, None)

        while True:
            if explode_tree(tree.traversal()):
                continue
            if split_tree(tree):
                continue
            break

        print('number: %s' % number)
        print('====================')
        print('tree: %s' % tree)
        print('====================')
        print('traversal: %s' % tree.traversal())

    print('Finished test: %s' % test.header)
    print('Answer: %s' % test.numbers)


def build_tree(number, parent):
    open_brackets = 0
    close_brackets = 0

    # Identify comma that splits root of tree
    for idx, c in enumerate(number):
        if c == '[':
            open_brackets += 1
        elif c == ']':
            close_brackets += 1
        elif c == ',' and open_brackets == close_brackets + 1:
            ln = number[1:idx]
            rn = number[idx+1:-1]
            lc = rc = lv = rv = None

            node = Node(parent=parent)

            if '[' not in ln:
                node.lv = int(ln)
            else:
                node.lc = build_tree(ln, node)
            if ']' not in rn:
                node.rv = int(rn)
            else:
                node.rc = build_tree(rn, node)

            return node

    raise ValueError('Invalid number: %s' % number)


def explode_tree(tree, depth):
    if depth >= 4 and tree.lv and tree.rv:
        traversal = tree.traversal()
        for i in range(len(traversal)-2):
            l, c, r = traversal[i], traversal[i+1], traversal[i+2]
            if c is tree:
                


def add(tree, number):
    root = Node(lv=None, rv=None)
    tree.parent = root
    root.lc = tree
    root.rc = build_tree(number, root)
    return root


if __name__ == '__main__':
    run()

