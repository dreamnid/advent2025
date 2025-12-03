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

INPUT_FILE='3-input.txt'
# INPUT_FILE='3a-example.txt'

input = [line for line in get_file_contents(INPUT_FILE)[0]]

with PrintTiming('a'):
    max_jolt = []
    for bank in input:
        cur_max: int | None = None
        for i in range(len(bank)-1):
            for j in range(i+1, len(bank)):
                # print(f'{i=} {j=}, {bank[i]=} {bank[j]=}')
                cur_num = int(f'{bank[i]}{bank[j]}')
                if cur_max is None or cur_num > cur_max:
                    cur_max = cur_num

        max_jolt.append(cur_max)

print('a', sum(max_jolt))

def solver(my_str: str, desired_len: int):
    if len(my_str) == desired_len:
        return int(my_str)

    # Greedily find the biggest digit that fits the desired length criteria
    max_digit = max([int(digit) for digit in my_str[:len(my_str) - desired_len + 1]])
    max_digit_idx = my_str.index(str(max_digit))

    # If we want a number that has more than one digit, then move to the next digit
    if 1 < desired_len:
        return int(f'{max_digit}{solver(my_str[max_digit_idx + 1:], desired_len-1)}')
    else:
        return max_digit

with PrintTiming('b'):
    max_jolt = []
    num_batts = 12
    for bank in input:
        # print(f'bank {bank=}')
        cur_max_str: str = bank[:num_batts]
        cur_max: int = int(cur_max_str)

        max_jolt.append(solver(bank, num_batts))

print('b', sum(max_jolt))
