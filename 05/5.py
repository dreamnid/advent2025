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

INPUT_FILE='5-input.txt'
# INPUT_FILE='5a-example.txt'
# INPUT_FILE='5a-exampleb.txt'

input1 = [[int(i) for i in line.split('-')] for line in get_file_contents(INPUT_FILE)[0]]
input1.sort(key=lambda x: x[0])

avail_ingredient_ids = [int(line) for line in get_file_contents(INPUT_FILE)[1]]

with PrintTiming('a'):
    total_fresh = 0
    for ingredient_id in avail_ingredient_ids:
        is_fresh = False
        for cur_fresh in input1:
            if cur_fresh[0] <= ingredient_id <= cur_fresh[1]:
                total_fresh += 1
                break

print('a', total_fresh)

with (PrintTiming('b')):
    total_fresh = 0
    seen = list()
    for cur_fresh in input1:
        old_total_fresh = total_fresh
        ranges_to_consider = list()
        for cur_seen in seen:
            if cur_seen[0] <= cur_fresh[0] <= cur_seen[1]:
                ranges_to_consider.append(cur_seen)
            elif cur_fresh[0] <= cur_seen[0] <= cur_fresh[1]:
                ranges_to_consider.append(cur_seen)

        match len(ranges_to_consider):
            case 0:
                pass
            case 1:
                if cur_seen[0] <= cur_fresh[0] <= cur_seen[1]:
                    if cur_fresh[1] > cur_seen[1]:
                        total_fresh += cur_fresh[1] - cur_seen[1]
                        cur_seen[1] = cur_fresh[1]
                elif cur_fresh[0] <= cur_seen[0] <= cur_fresh[1]:
                    total_fresh += cur_seen[0] - cur_fresh[0]
                    cur_seen[0] = cur_fresh[0]
                    if cur_fresh[1] > cur_seen[1]:
                        total_fresh += cur_fresh[1] - cur_seen[1]
                        cur_seen[1] = cur_fresh[1]
            case 2:
                total_fresh += ranges_to_consider[1][0] - ranges_to_consider[0][1]

                combined_seen = [ranges_to_consider[0][0], ranges_to_consider[1][0]]
                seen = [n for n in seen if set(n) not in [set(ranges_to_consider[0]), set(ranges_to_consider[1])]]

                if cur_fresh[1] > ranges_to_consider[1][1]:
                    total_fresh += cur_fresh[1] - ranges_to_consider[1][1]
                    combined_seen[1] = cur_fresh[1]

                seen.append(combined_seen)

            case _:
                raise ValueError()


        if old_total_fresh == total_fresh and not ranges_to_consider:
            total_fresh += cur_fresh[1] - cur_fresh[0] + 1
            seen.append(cur_fresh)

print('b', total_fresh)
