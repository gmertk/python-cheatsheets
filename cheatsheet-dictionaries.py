#  ____  _      _   _                        _             
# |  _ \(_) ___| |_(_) ___  _ __   __ _ _ __(_) ___  ___   
# | | | | |/ __| __| |/ _ \| '_ \ / _` | '__| |/ _ \/ __|  
# | |_| | | (__| |_| | (_) | | | | (_| | |  | |  __/\__ \  
# |____/|_|\___|\__|_|\___/|_| |_|\__,_|_|  |_|\___||___/  
#    
# https://docs.python.org/2/library/stdtypes.html#typesmapping     
                                              
print '\n-- dictionaries'

d = {'a': 1, 'b': 2}
print d['a'] # if key doesn't exist, raise KeyError exception
del d['a'] # if key doesn't exist, raise KeyError exception

# iterate
d = {'a': 1, 'b': 2}
for key, value in d.items():
    print key, ':', value

for key in d:
    print key, d[key]

# d.fromkeys(iterable[,value=None]) -> dict: with keys from iterable and all same value
d = d.fromkeys(['a', 'b'], 1)
print d  # {'a': 1, 'b': 1}


# d.clear() -> removes all items from d
d = {'a': 1, 'b': 2}
d.clear()
print d  # {}


# d.items() -> list: copy of d's list of (key, item) pairs
d = {'a': 1, 'b': 2}
print d.items()  # [('a', 1), ('b', 2)]


# d.keys() -> list: copy of d's list of keys
d = {'a': 1, 'b': 2}
print d.keys()  # ['a', 'b']


# d.values() -> list: copy of d's list of values
d = {'a': 1, 'b': 2}
print d.values()  # [1, 2]


# d.get(key,defval) -> value: d[key] if key in d, else defval
d = {'a': 1, 'b': 2}
print d.get("c", 3)  # 3
print d  # {'a': 1, 'b': 2} 


# d.setdefault(key[,defval=None]) -> value: if key not in d set d[key]=defval, return d[key]
d = {'a': 1, 'b': 2}
print 'd.setdefault("c", []) returns ' + str(d.setdefault("c", 3)) + ' d is now ' + str(d) 
# d.setdefault("c", []) returns 3 d is now {'a': 1, 'c': 3, 'b': 2}


#d.pop(key[,defval]) -> value: del key and returns the corresponding value. If key is not found, defval is returned if given, otherwise KeyError is raised
d = {'a': 1, 'b': 2}
print 'd.pop("b", 3) returns ' + str(d.pop("b", 3)) + ' d is now ' + str(d)
# d.pop("b", 3) returns 2 d is now {'a': 1}
print 'd.pop("c", 3) returns ' + str(d.pop("c", 3)) + ' d is still ' + str(d) 
# d.pop("c", 3) returns 3 d is still {'a': 1}


# sort on values
import operator
x = {1: 4, 5: 4, 4: 4}
sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
print 'sorted(x.items(), key=operator.itemgetter(1)) sorts on values ' + str(sorted_x)


# sort on keys instead of values:
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))


# max of values
d = {'a':1000, 'b':3000, 'c': 100}
print 'key of max value is ' + max(d.keys(), key=(lambda key: d[key]))


# inverse a map
for k,v in d.iteritems():
    print k
    print v
print 'inverse of d is ' + str(dict((v, k) for k, v in d.iteritems()))


# use-cases for setdefault
data = [(1, "a"), (2, "b")]
# really verbose
new = {}
for (key, value) in data:
    if key in new.keys():
        new[key].append( value )
    else:
        new[key] = [value]


# easy with setdefault
new = {}
for (key, value) in data:
    group = new.setdefault(key, []) # key might exist already
    group.append( value )


# even simpler with defaultdict 
from collections import defaultdict

new = defaultdict(list)
for (key, value) in data:
    new[key].append( value ) # all keys have a default already