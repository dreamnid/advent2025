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

INPUT_FILE='2-input.txt'
# INPUT_FILE='2a-example.txt'

input = get_file_contents(INPUT_FILE)[0][0].split(',')

with PrintTiming('a'):
    invalid_ids = []
    for cur_range_str in input:
        cur_range_start, cur_range_stop = cur_range_str.split('-')
        for i in range(int(cur_range_start), int(cur_range_stop) + 1):
            i_str = str(i)
            if len(i_str) % 2 == 1:
                continue

            mid_pt = len(i_str) // 2

            invalid = True
            for j in range(mid_pt):
                invalid &= i_str[j] == i_str[mid_pt+j]
                if not invalid:
                    break

            if invalid:
                invalid_ids.append(i)

print('a:', sum(invalid_ids))

with PrintTiming('b'):
    invalid_ids = []
    for cur_range_str in input:
        cur_range_start, cur_range_stop = cur_range_str.split('-')
        for i in range(int(cur_range_start), int(cur_range_stop) + 1):
            i_str = str(i)
            mid_pt = len(i_str) // 2

            for j in range(1, mid_pt + (1 if mid_pt % 2 == 0 else 1)):
                multi = 1
                while True:
                    crafted_str = i_str[:j] * (1 + multi)
                    crafted_num = int(crafted_str)
                    if crafted_num not in invalid_ids and int(cur_range_start) <= crafted_num <= int(cur_range_stop):
                        invalid_ids.append(crafted_num)
                    elif crafted_num > int(cur_range_stop):
                        break
                    multi += 1

# print(invalid_ids)
print('b:', sum(invalid_ids))
