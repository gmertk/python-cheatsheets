#   ___                                         
#  / _ \ _   _  ___ _   _  ___  ___             
# | | | | | | |/ _ \ | | |/ _ \/ __|            
# | |_| | |_| |  __/ |_| |  __/\__ \            
#  \__\_\\__,_|\___|\__,_|\___||___/            
# 
# https://docs.python.org/2/library/collections.html#collections.deque

print '--queues'
from collections import deque

d = deque('ghi')
for elem in d:                   # iterate over the deque's elements
    print elem.upper()

d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
print d

d.pop()                          # return and remove the rightmost item # j
d.popleft()                      # return and remove the leftmost item # f
print list(d)                    # list the contents of the deque
print 'g' in d                   # search the deque

print d
d.extend('jkl')                  # add multiple elements at once
print d
d.extendleft('abc')              # extendleft() reverses the input order
print d

d.rotate(1)                      # right rotation
print d

d.rotate(-1)                     # left rotation
print d

print len(d)

a = deque(reversed(d))               # make a new deque in reverse order
print a

del a[0]
print a


#  ____       _            _ _            ___                              
# |  _ \ _ __(_) ___  _ __(_) |_ _   _   / _ \ _   _  ___ _   _  ___  ___  
# | |_) | '__| |/ _ \| '__| | __| | | | | | | | | | |/ _ \ | | |/ _ \/ __| 
# |  __/| |  | | (_) | |  | | |_| |_| | | |_| | |_| |  __/ |_| |  __/\__ \ 
# |_|   |_|  |_|\___/|_|  |_|\__|\__, |  \__\_\\__,_|\___|\__,_|\___||___/ 
#                                |___/                                     
#
#https://docs.python.org/2/library/heapq.html

import heapq

print '\n--heaps'

heap = []
heapq.heappush(heap, 2)
print heap 

a = [3, 2, 1]
heapq.heapify(a)
print a

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

b = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print heapsort(b)

#nlargest(n,iterable) -> list: n largest from iterable
print heapq.nlargest(3, b)

print heapq.nsmallest(3, b)
