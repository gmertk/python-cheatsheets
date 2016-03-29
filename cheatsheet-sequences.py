#  ____                                                        
# / ___|  ___  __ _ _   _  ___ _ __   ___ ___  ___              
# \___ \ / _ \/ _` | | | |/ _ \ '_ \ / __/ _ \/ __|             
#  ___) |  __/ (_| | |_| |  __/ | | | (_|  __/\__ \             
# |____/ \___|\__, |\__,_|\___|_| |_|\___\___||___/             
#                |_|                                            
#
# https://docs.python.org/2/tutorial/datastructures.html
   
print '-- sequences'

a = ['foo', 'bar', 'baz']
# iterate 
for i in a:
    print i

for i in range(len(a)):
    print i, a[i]

# enumerate arrays
for i, j in enumerate(a):
    print i, j 

# Declare a list which is mutable : [item[,...]]
a = []
a = list()

# Declare a tuple which is immutable : (item[,...])
a = ()

# From string
a = list('abcdef')

# Checking if a list is empty
if a:
    print 'a is not empty'
else:
    print 'a is empty'

# (item,) : one item tuple.
a = (1,) 

# seq1 + seq2 -> concatenation of seq1 and seq2
a = [1] + [2]
print '[1] + [2] = ' + str(a)

# sequence * n -> concatenation of sequence duplicated n times
a = [1] * 5
print '[1] * 5 = ' + str(a)

# copy list
b = a[:]
b = list(a)
print 'copy of a list can be created with a[:] or list(a)'

# sum(container) -> value: sum of items (items must be number-compatible)
a = sum([1, 2, 3])
print 'sum([1, 2, 3]) = ' + str(a)

# min(container) -> value: smallest item in container
a = min([1, 2, 3, 0])
print 'min([1, 2, 3, 0]) = ' + str(a)

# reversed(sequence) -> iterator throught sequence in reverse order
a = reversed([1, 2, 3])
for i in a:
    print i,
print 

# sorted(sequence[,cmp[,key[,reverse]]]) -> list: new list, sorted items from iterable - see list.sorted()
a = [5, 2, 3, 1, 4]
print 'a = [5, 2, 3, 1, 4] and sorted(a) returns a new sorted list ' + str(sorted(a))

# a key parameter to specify a function to be called on each list element prior to making comparisons.
print sorted("a test string Mert gunay".split(), key=str.lower)

student_tuples = [
   ('john', 'A', 15),
   ('jane', 'B', 12),
   ('dave', 'B', 10),
]

student_objects = [
   Student('john', 'A', 15),
   Student('jane', 'B', 12),
   Student('dave', 'B', 10),
]

print sorted(student_tuples, key=lambda student: student[2])   # sort by age

from operator import itemgetter, attrgetter, methodcaller
print sorted(student_tuples, key=itemgetter(2))
print sorted(student_tuples, key=itemgetter(1,2))

print sorted(student_objects, key=attrgetter('age'))
print sorted(student_objects, key=attrgetter('grade', 'age'))

# map(fct,sequence,...) -> list: new list where ith item is fct(ith items of sequence(s))
celsius = [39.2, 36.5]
fahrenheit = map(lambda x: (float(9)/5)*x + 32, celsius)
print 'map(lambda x: (float(9)/5)*x + 32, [39.2, 36.5]) = ' + str(fahrenheit)

# reduce(fct,sequence[,initializer]) -> value: fct applied cumulatively
a = reduce(lambda x,y: x+y, [1, 2, 3])
print 'reduce(lambda x,y: x+y, [1, 2, 3]) = ' + str(a)

a = reduce(lambda a,b: a if (a > b) else b, [1, 3, 5, 2])
print 'reduce(lambda a,b: a if (a > b) else b, [1, 3, 5, 2]) = ' + str(a)

# filter1(fct,sequence) -> list: new list where fct(item) is True. Use None fct for a boolean test on items
a = filter(lambda a: a % 2 == 0, [1, 3, 5, 2])
print 'filter(lambda a: a % 2 == 0, [1, 3, 5, 2]) = ' + str(a)

#zip(sequence,...) -> list: list of tuples, ith tuple contains ith items of each sequences
a = zip([1,2,3], ["a", "b", "c"])
print 'zip([1,2,3], ["a", "b", "c"]) is ' + str(a)

# slice [start:stop[:step]] syntax
# a[start:end]  items start through end-1
# a[start:]     items start through the rest of the array
# a[:end]       items from the beginning through end-1
# a[:]          a copy of the whole array
# a[start:end:step]  start through not past end, by step
# a[-1]     last item in the array
# a[-2:]    last two items in the array
# a[:-2]    everything except the last two items
a = [0, 1, 2, 3]
print 'a[:] = ' + str(a[:])
print 'a[0:] = ' + str(a[0:])
print 'a[:2] = ' + str(a[:2])
print 'a[:-1] = ' + str(a[:-1])
print 'a[::-1] = ' + str(a[::-1])

# seq[start:stop:step]=expr
a[0:2] = [9]
print 'a[0:2] = [9] makes a = ' + str(a) 

# seq.append(item) : add item at end of sequence
a = [0, 1, 2, 3]
a.append(5)
print 'a = [0, 1, 2, 3] - after a.append(5), a becomes ' + str(a)

# seq.insert(index,item) : item inserted at index
a = [0, 1, 2, 3]
a.insert(0, 5)
print 'a = [0, 1, 2, 3] - after a.insert(0, 5), a becomes ' + str(a)

# seq.remove(expr) : remove first expr item from sequence 
a = ["a", "b", "c", "b"]
a.remove("b")
print 'a = ["a", "b", "c", "b"] - after a.remove("b"), a becomes ' + str(a)

# seq.pop([index]) -> item: remove and return item at index (default -1)
a = [0, 1, 2, 3]
b = a.pop(2)
print 'a = [0, 1, 2, 3] - after a.pop(2), a becomes ' + str(a) + ' pop(2) returns ' + str(b) 

# seq.count(expr) -> int: number of expr items in sequence 
print 'a.count(3) = ' + str(a.count(3))

# seq.index(expr[,start[,stop]]) -> int: first index of expr item or ValueError 
try:
    print 'a.index(5) = ' + str(a.index(5))
except ValueError:
    print 'Not found'

# seq.reverse() : items reversed in place
a = [0, 1, 2, 3]
a.reverse()
print 'a = [0, 1, 2, 3] - after a.reverse(), a becomes ' + str(a)
 
# seq.sort([cmp][,key][,reverse]) : items sorted in place - cmp : custom comparison fct(a,b), retval <0 or = 0 or >0 - key : name of items attribute to compare - reverse : bool
a = [0, 3, 1, 2]
a.sort()
print 'a = [0, 3, 1, 2] - after a.sort(), a becomes ' + str(a)

# del seq[index] : remove item from sequence
a = [0, 1, 2, 3]
del a[2]
print 'a = [0, 1, 2, 3] - after del a[2], a becomes ' + str(a)
 
# del seq[start:stop[:step]] : remove items from sequence
a = [0, 1, 2, 3]
del a[1:3]
print a  # [0, 3]
