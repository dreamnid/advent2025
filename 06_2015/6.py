#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
from collections.abc import Callable, Collection, Iterable, Sequence
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

INPUT_FILE='6-input.txt'
# INPUT_FILE='6a-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]

grid = defaultdict(lambda: defaultdict(bool))

with PrintTiming('a') as t:
    for line in input:
        splitted = line.split(' ')
        if splitted[0] == 'turn':
            start_coord = tuple(map(int, splitted[2].split(',')))
            end_coord = tuple(map(int, splitted[4].split(',')))

            match splitted[1]:
                case 'on':
                    mode = True
                case 'off':
                    mode = False
                case _:
                    raise ValueError(line)

        else:
            # toggle
            start_coord = tuple(map(int, splitted[1].split(',')))
            end_coord = tuple(map(int, splitted[3].split(',')))
            mode = None

        for row in range(start_coord[0], end_coord[0] + 1):
            for col in  range(start_coord[1], end_coord[1] + 1):
                grid[row][col] = mode if mode is not None else not grid[row][col]


    count_on = 0
    for row in grid.values():
        for col in row.values():
            if col:
                count_on += 1
        #     print(col, end=' ')
        # print()

print('a:', count_on)

with PrintTiming('b') as t:
    grid = defaultdict(lambda: defaultdict(int))
    for line in input:
        splitted = line.split(' ')
        if splitted[0] == 'turn':
            start_coord = tuple(map(int, splitted[2].split(',')))
            end_coord = tuple(map(int, splitted[4].split(',')))

            match splitted[1]:
                case 'on':
                    mode = 1
                case 'off':
                    mode = -1
                case _:
                    raise ValueError(line)

        else:
            # toggle
            start_coord = tuple(map(int, splitted[1].split(',')))
            end_coord = tuple(map(int, splitted[3].split(',')))
            mode = 2

        for row in range(start_coord[0], end_coord[0] + 1):
            for col in  range(start_coord[1], end_coord[1] + 1):
                grid[row][col] += mode
                if mode < 0:
                    grid[row][col] = max(0, grid[row][col])

    total_brightness = 0
    for row in grid.values():
        for col in row.values():
            total_brightness += col

print('b', total_brightness)
