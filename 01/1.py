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

INPUT_FILE='1-input.txt'
# INPUT_FILE='1a-example.txt'
# INPUT_FILE='1a-example2.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]

lock_pos = 50
counter_0 = 0

for line in input:
    num_rotations = int(line[1:])
    match line[0]:
        case 'L':
            lock_pos -= num_rotations
        case _:
            lock_pos += num_rotations

    lock_pos %= 100
    if 0 == lock_pos:
        counter_0 += 1

print('a: num zeros reached:', counter_0)
print()

lock_pos = 50
counter_0 = 0

for line in input:
    num_rotations = int(line[1:])
    num_full_rotations = num_rotations // 100
    old_lock_pos = lock_pos
    match line[0]:
        case 'L':
            # print('old_lock_pos L', lock_pos, num_rotations, counter_0)
            # print('new_lock_pos L', lock_pos, num_rotations, counter_0)
            if lock_pos != 0 and (num_rotations % 100) > lock_pos:
                # Will rotate past 0
                # print('L +1')
                counter_0 += 1

            lock_pos -= num_rotations
        case _:
            if (100 - lock_pos) < (num_rotations % 100):
                # print('R +1')
                counter_0 += 1
            lock_pos += num_rotations

    # print(f'{lock_pos % 100=}, {num_rotations=}, {num_full_rotations=}, {counter_0=}')
    lock_pos %= 100
    if 0 == lock_pos:
        counter_0 += 1

    counter_0 += num_full_rotations
    # print('new counter_0=', counter_0)
    # print()

print('b: num zeros reached:', counter_0)
