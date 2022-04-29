import random
from collections import defaultdict
import itertools
import time


"""
s = []
i = 0
while i < 10000000:
    i += 1
    a = (random.randint(0, 9), random.randint(0, 9))
    s.append(a)

import time

start = time.time()

d = {}
for k, v in s:
    d.setdefault(k, []).append(v)
# 2.15 s ± 5.47 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
print("Uno: ", time.time()- start)


start = time.time()
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
# 1.25 s ± 5.42 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
print("Dos: ", time.time()- start)


start = time.time()
d = {}
for k, v in s:
    if k not in d:
        d[k] = []
    d[k].append(v)
# 1.56 s ± 36.4 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
print("Tres: ", time.time()- start)

"""

start = time.time()

#list(itertools.repeat(10000000,10))




print("Tres: ", time.time()- start)