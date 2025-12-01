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
    match line[0]:
        case 'L':
            while num_rotations:
                # print('old_lock_pos L', lock_pos, num_rotations, counter_0)
                if num_rotations > lock_pos:
                    num_rotations -= lock_pos
                    if lock_pos > 0:
                        counter_0 += 1
                    lock_pos = 100
                elif num_rotations == lock_pos:
                    lock_pos = 0
                    counter_0 += 1
                    num_rotations = 0
                else:
                    lock_pos -= num_rotations
                    num_rotations = 0
                # print('new_lock_pos L', lock_pos, num_rotations, counter_0)
        case _:
            while num_rotations:
                # print('old_lock_pos R', lock_pos, num_rotations, counter_0)
                if num_rotations > 100 - lock_pos:
                    num_rotations -= 100 - lock_pos
                    lock_pos = 0
                    counter_0 += 1
                elif num_rotations == 100 - lock_pos:
                    lock_pos = 0
                    counter_0 += 1
                    num_rotations = 0
                else:
                    lock_pos += num_rotations
                    num_rotations = 0
                # print('new_lock_pos R', lock_pos, num_rotations, counter_0)

    # print('step lock_pos', lock_pos, counter_0)
    # print()

    # num_full_rotations = int(lock_pos / 100.0)
    # print('lock_pos', lock_pos, lock_pos % 100, int(lock_pos / 100), num_full_rotations, counter_0)
    # lock_pos %= 100
    # if 0 == lock_pos:
    #     counter_0 += 1

    # counter_0 += num_full_rotations
    # if num_full_rotations > 0 and lock_pos == 0:
    #     counter_0 -= 1
    # print('new counter_0', counter_0)

print('b: num zeros reached:', counter_0)
