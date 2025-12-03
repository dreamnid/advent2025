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

# print('a', sum(max_jolt))

with PrintTiming('b'):
    max_jolt = []
    num_batts = 12
    for bank in input:
        print(f'bank {bank=}')
        cur_max_str: str = bank[:num_batts]
        cur_max: int = int(cur_max_str)
        # ptrs = list(range(num_batts))

        # for i0 in range(len(bank)-num_batts+1):
        #     if bank[i0] < cur_max_str[0]:
        #         continue
        #     for i1 in range(i0+1, len(bank)-num_batts+2):
        #         if int(f'{bank[i0]}{bank[i1]}') < int(cur_max_str[:2]):
        #             continue
        #         for i2 in range(i1+1, len(bank) - num_batts + 3):
        #             if int(f'{bank[i0]}{bank[i1]}{bank[i2]}') < int(cur_max_str[:3]):
        #                 continue
        #             for i3 in range(i2 + 1, len(bank) - num_batts + 4):
        #                 if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}') < int(cur_max_str[:4]):
        #                     continue
        #                 for i4 in range(i3 + 1, len(bank) - num_batts + 5):
        #                     if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}') < int(cur_max_str[:5]):
        #                         continue
        #                     for i5 in range(i4 + 1, len(bank) - num_batts + 6):
        #                         if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}') < int(cur_max_str[:6]):
        #                             continue
        #                         for i6 in range(i5 + 1, len(bank) - num_batts + 7):
        #                             if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}')  < int(cur_max_str[:7]):
        #                                 continue
        #                             for i7 in range(i6 + 1, len(bank) - num_batts + 8):
        #                                 if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}{bank[i7]}') < int(cur_max_str[:8]):
        #                                     continue
        #                                 for i8 in range(i7 + 1, len(bank) - num_batts + 9):
        #                                     if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}{bank[i7]}{bank[i8]}') < int(cur_max_str[:9]):
        #                                         continue
        #                                     for i9 in range(i8 + 1, len(bank) - num_batts + 10):
        #                                         if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}{bank[i7]}{bank[i8]}{bank[i9]}') < int(cur_max_str[:10]):
        #                                             continue
        #                                         for i10 in range(i9 + 1, len(bank) - num_batts + 11):
        #                                             if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}{bank[i7]}{bank[i8]}{bank[i9]}{bank[i10]}') < int(cur_max_str[:11]):
        #                                                 continue
        #                                             for i11 in range(i10 + 1, len(bank) - num_batts + 12):
        #                                                 cur_num = int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}{bank[i7]}{bank[i8]}{bank[i9]}{bank[i10]}{bank[i11]}')
        #                                                 if cur_num > cur_max:
        #                                                     cur_max = cur_num
        #                                                     cur_max_str = str(cur_num)
        max_i0 = None
        for i0 in range(len(bank)-num_batts+1):
            if max_i0 is not None and int(bank[i0]) < max_i0:
                continue
            max_i0 = int(bank[i0])
            if bank[i0] < cur_max_str[0]:
                continue
            max_i1 = None
            for i1 in range(i0+1, len(bank)-num_batts+2):
                if max_i1 is not None and int(bank[i1]) < max_i1:
                    continue
                max_i1 = int(bank[i1])
                # if int(f'{bank[i0]}{bank[i1]}') < int(cur_max_str[:2]):
                #     continue
                max_i2 = None
                for i2 in range(i1+1, len(bank) - num_batts + 3):
                    if max_i2 is not None and int(bank[i2]) < max_i2:
                        continue
                    max_i2 = int(bank[i2])
                    # if int(f'{bank[i0]}{bank[i1]}{bank[i2]}') < int(cur_max_str[:3]):
                    #     continue

                    max_i3 = None
                    for i3 in range(i2 + 1, len(bank) - num_batts + 4):
                        if max_i3 is not None and int(bank[i3]) < max_i3:
                            continue
                        max_i3 = int(bank[i3])
                        # if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}') < int(cur_max_str[:4]):
                        #     continue
                        max_i4 = None
                        for i4 in range(i3 + 1, len(bank) - num_batts + 5):
                            if max_i4 is not None and int(bank[i4]) < max_i4:
                                continue
                            max_i4 = int(bank[i4])
                            # if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}') < int(cur_max_str[:5]):
                            #     continue
                            max_i5 = None
                            for i5 in range(i4 + 1, len(bank) - num_batts + 6):
                                if max_i5 is not None and int(bank[i5]) < max_i5:
                                    continue
                                max_i5 = int(bank[i5])
                                # if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}') < int(cur_max_str[:6]):
                                #     continue
                                max_i6 = None
                                for i6 in range(i5 + 1, len(bank) - num_batts + 7):
                                    if max_i6 is not None and int(bank[i6]) < max_i6:
                                        continue
                                    max_i6 = int(bank[i6])
                                    # if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}')  < int(cur_max_str[:7]):
                                    #     continue
                                    max_i7 = None
                                    for i7 in range(i6 + 1, len(bank) - num_batts + 8):
                                        if max_i7 is not None and int(bank[i7]) < max_i7:
                                            continue
                                        max_i7 = int(bank[i7])
                                        # if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}{bank[i7]}') < int(cur_max_str[:8]):
                                        #     continue
                                        max_i8 = None
                                        for i8 in range(i7 + 1, len(bank) - num_batts + 9):
                                            if max_i8 is not None and int(bank[i8]) < max_i8:
                                                continue
                                            max_i8 = int(bank[i8])
                                            # if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}{bank[i7]}{bank[i8]}') < int(cur_max_str[:9]):
                                            #     continue
                                            max_i9 = None
                                            for i9 in range(i8 + 1, len(bank) - num_batts + 10):
                                                if max_i9 is not None and int(bank[i9]) < max_i9:
                                                    continue
                                                max_i9 = int(bank[i9])
                                                # if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}{bank[i7]}{bank[i8]}{bank[i9]}') < int(cur_max_str[:10]):
                                                #     continue
                                                max_i10 = None
                                                for i10 in range(i9 + 1, len(bank) - num_batts + 11):
                                                    if max_i10 is not None and int(bank[i10]) < max_i10:
                                                        continue
                                                    max_i10 = int(bank[i10])
                                                    # if int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}{bank[i7]}{bank[i8]}{bank[i9]}{bank[i10]}') < int(cur_max_str[:11]):
                                                    #     continue
                                                    max_i11 = None
                                                    for i11 in range(i10 + 1, len(bank) - num_batts + 12):
                                                        if max_i11 is not None and int(bank[i11]) < max_i11:
                                                            continue
                                                        max_i11 = int(bank[i11])
                                                        cur_num = int(f'{bank[i0]}{bank[i1]}{bank[i2]}{bank[i3]}{bank[i4]}{bank[i5]}{bank[i6]}{bank[i7]}{bank[i8]}{bank[i9]}{bank[i10]}{bank[i11]}')
                                                        if cur_num > cur_max:
                                                            cur_max = cur_num
                                                            cur_max_str = str(cur_num)

        max_jolt.append(cur_max)

print('b', max_jolt, sum(max_jolt))
