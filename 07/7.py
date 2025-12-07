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

INPUT_FILE='7-input.txt'
# INPUT_FILE='7a-example.txt'

input = [list(line) for line in get_file_contents(INPUT_FILE)[0]]

with PrintTiming('a'):
    total_split = 0
    for i, line in enumerate(input[1:], start=1):
        for j, cur_char in enumerate(line):
            if input[i-1][j] in ['S', '|']:
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