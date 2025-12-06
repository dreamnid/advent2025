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
            case '+':
                op = operator.add
            case _:
                raise ValueError()

        total += reduce(op, list(map(int, line[:-1])))

print('a', total)
