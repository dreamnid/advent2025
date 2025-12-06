#!/usr/bin/env python3
import operator
from collections import Counter, defaultdict, deque
from collections.abc import Callable, Collection, Iterable, Sequence
from dataclasses import dataclass
from functools import partial, reduce
from itertools import chain, cycle, takewhile, accumulate
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

input = np.array([' '.join(line.split()).split(' ') for line in get_file_contents(INPUT_FILE)[0]])

input = input.T

with PrintTiming('a'):
    total = 0
    for line in input:
        match line[-1]:
            case '*':
                op = operator.mul
                fill = 1
            case '+':
                op = operator.add
                fill = 0
            case _:
                raise ValueError()

        max_digits = 0
        for el in line[:-1]:
            if len(el) > max_digits:
                max_digits = len(el)

        total += reduce(op, list(map(int, line[:-1])))

print('a', total)

input = [line for line in get_file_contents(INPUT_FILE)[0]]
with PrintTiming('b'):
    total = 0
    width = max(len(l) for l in input)
    height = len(input) - 1
    buffers = [''] * height
    for i in range(width):
        cur_char = input[-1][i] if i < len(input[-1]) else ' '
        match cur_char:
            case '*':
                op = operator.mul
            case '+':
                op = operator.add
            case ' ':
                pass

        for j in range(height):
            try:
                buffers[i % height] += input[j][i]
            except IndexError:
                pass

        if i + 1 == width or (i+1 < len(input[-1]) and input[-1][i+1] in ('*', '+')):
            # process
            problem_solution = reduce(op, [int(n) for n in buffers if n.strip()])
            total += problem_solution
            buffers = [''] * height

print('b', total)