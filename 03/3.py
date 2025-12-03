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
    max_digit = int(my_str[0])
    max_digit_indices = list()
    # Find the biggest digit that fits the desired length criteria
    for i, digit in enumerate(my_str[:len(my_str) - desired_len+1]):
        int_digit = int(digit)
        if int_digit == max_digit:
            max_digit_indices.append(i)
        elif int_digit > max_digit:
            max_digit = int_digit
            max_digit_indices = [i]

    # print(my_str, max_digit, max_digit_indices)

    # If we want a number that has more than one digit, then move to the next digit
    if desired_len > 1:
        recurse_result = []
        for i in max_digit_indices:
           recurse_result.append(int(f'{max_digit}{solver(my_str[i+1:], desired_len-1)}'))
        return max(recurse_result)
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
