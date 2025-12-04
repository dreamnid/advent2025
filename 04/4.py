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

INPUT_FILE='4-input.txt'
# INPUT_FILE='4a-example.txt'

input = add_padding([[char for char in line] for line in get_file_contents(INPUT_FILE)[0]], '#')

with PrintTiming('a'):
    valid = 0
    for i, row in enumerate(input):
        for j, val in enumerate(row):
            if val in ('#', '.'):
                continue

            if sum(n == '@' for n in get_neighbors(input, i, j)) < 4:
                valid += 1
                # row[j] = 'x'

print('a', valid)
