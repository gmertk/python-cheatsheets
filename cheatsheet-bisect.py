#  ____             _           _   _     _     _        
# / ___|  ___  _ __| |_ ___  __| | | |   (_)___| |_ ___  
# \___ \ / _ \| '__| __/ _ \/ _` | | |   | / __| __/ __| 
#  ___) | (_) | |  | ||  __/ (_| | | |___| \__ \ |_\__ \ 
# |____/ \___/|_|   \__\___|\__,_| |_____|_|___/\__|___/ 
# 
# https://docs.python.org/2/library/bisect.html

import bisect

a = [0, 1, 2, 5]

# bisect.bisect_left(a, x, lo=0, hi=len(a))
i = bisect.bisect_left(a, 2)
print i

# bisect.bisect_right(a, x, lo=0, hi=len(a))
i = bisect.bisect_right(a, 2)
print i

# bisect.insort_left(a, x, lo=0, hi=len(a))
i = bisect.bisect(a, 2)
print i

print a

a.insert(i, 2)
print a

# bisect.insort_left(a, x, lo=0, hi=len(a))
# bisect.insort_right(a, x, lo=0, hi=len(a))
# bisect.insort(a, x, lo=0, hi=len(a))
bisect.insort_left(a, 3)
print a

bisect.insort_left(a, 3, 0, 1)
print a


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError
    
def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])
keys = [r[1] for r in data]         # precomputed list of keys
print data[bisect.bisect_left(keys, 0)]

print data[bisect.bisect_left(keys, 1)]

print data[bisect.bisect_left(keys, 5)]
