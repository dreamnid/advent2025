#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
from collections.abc import Callable, Collection, Iterable, Sequence
from copy import deepcopy
from dataclasses import dataclass
from functools import partial, reduce
from itertools import chain, cycle, takewhile
import math
from operator import mul, ge, gt, itemgetter, le, lt
import os
import pprint
import re
from time import time
from typing import NamedTuple

from humanize import intcomma
import numpy as np
import pyparsing as pp
import pandas as pd

# Fix path so we can do a relative import: https://stackoverflow.com/a/27876800
if __name__ == '__main__':
    if not __package__:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

        # Relative imports here
        from util import *


class Pos(NamedTuple):
    row: int
    col: int


INPUT_FILE='7-input.txt'
# INPUT_FILE='7a-example.txt'

input = [list(line) for line in get_file_contents(INPUT_FILE)[0]]

with PrintTiming('a'):
    input_a = deepcopy(input)
    total_split = 0
    for i, line in enumerate(input_a[1:], start=1):
        for j, cur_char in enumerate(line):
            if input_a[i-1][j] in ['S', '|']:
                match cur_char:
                    case '.':
                        line[j] = '|'
                    case '^':
                        total_split += 1
                        if line[j-1] == '.':
                            line[j-1] = '|'
                        if line[j+1] == '.':
                            line[j+1] = '|'

print('a', total_split)
del input_a


def find_split(pos: Pos, input):
    for i in range(pos.row + 1, len(input)):
        if input[i][pos.col] == '^':
            return Pos(i, pos.col)

    return None


with PrintTiming('b'):

    # paths: list[list[Pos]] = [[Pos(0, input[0].index('S'))]]
    #
    # for i, line in enumerate(input[1:], start=1):
    #     print(f'{i=}')
    #     new_paths = list()
    #     for path in paths:
    #         last_node = path[-1]
    #         match input[i][last_node.col]:
    #             case '.':
    #                 path += Pos(i, last_node.col),
    #             case '^':
    #                 new_paths.append(deepcopy(path) + [Pos(i, last_node.col + 1)])
    #                 path += Pos(i, last_node.col-1),
    #     # print(paths)
    #     if new_paths:
    #         paths.extend(new_paths)

    start_positions: list[Pos] = [Pos(0, input[0].index('S'))]

    total_paths = 1
    while start_positions:
        cur_pos = start_positions.pop()

        if (split_res := find_split(cur_pos, input)) is not None:
            total_paths += 1
            start_positions.append(Pos(split_res.row, split_res.col-1))
            start_positions.append(Pos(split_res.row, split_res.col+1))

        # pprint.pprint(start_positions)

print('b', total_paths)
