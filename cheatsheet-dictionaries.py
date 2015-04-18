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

print 'd = {"a": 1, "b": 2} - after del d["a"], d becomes ' + str(d)
print 'dict([("a", 1), ("b", 2)]) creates' + str( dict([("a", 1), ("b", 2)]) )

# iterate
d = {'a': 1, 'b': 2}
for key, value in d.items():
    print key, 'corresponds to', value

for key in d:
    print key, d[key]

# d.fromkeys(iterable[,value=None]) -> dict: with keys from iterable and all same value
d = d.fromkeys(['a', 'b'], 1)
print 'd.fromkeys(["a", "b"], 1) returns ' + str(d)

# d.clear() -> removes all items from d
d = {'a': 1, 'b': 2}
d.clear()
print 'd = {"a": 1, "b": 2} - after d.clear(), d becomes ' + str(d)

# d.items() -> list: copy of d's list of (key, item) pairs
d = {'a': 1, 'b': 2}
a = d.items()
print 'd.items() returns ' + str(a)

# d.keys() -> list: copy of d's list of keys
d = {'a': 1, 'b': 2}
a = d.keys()
print 'd.keys() returns ' + str(a)

# d.values() -> list: copy of d's list of values
d = {'a': 1, 'b': 2}
a = d.values()
print 'd.values() returns ' + str(a)

# d.get(key,defval) -> value: d[key] if key in d, else defval
d = {'a': 1, 'b': 2}
print 'd.get("c", 3) returns ' + str(d.get("c", 3)) + ' d is still ' + str(d)

# d.setdefault(key[,defval=None]) -> value: if key not in d set d[key]=defval, return d[key]
d = {'a': 1, 'b': 2}
print 'd.setdefault("c", 3) returns ' + str(d.setdefault("c", 3)) + ' d is now ' + str(d) 

#d.pop(key[,defval]) -> value: del key and returns the corresponding value. If key is not found, defval is returned if given, otherwise KeyError is raised
d = {'a': 1, 'b': 2}
print 'd.pop("b", 3) returns ' + str(d.pop("b", 3)) + ' d is now ' + str(d) 
print 'd.pop("c", 3) returns ' + str(d.pop("c", 3)) + ' d is still ' + str(d) 

# sort on values
import operator
x = {1: 2, 3: 4, 4: 3}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print 'sorted(x.items(), key=operator.itemgetter(1)) sorts on values ' + str(sorted_x)

# sort on keys instead of values:
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))

# max of values
d = {'a':1000, 'b':3000, 'c': 100}
print 'key of max value is ' + max(d.iterkeys(), key=(lambda key: d[key]))

# inverse a map
print 'inverse of d is ' + str(dict((v, k) for k, v in d.iteritems()))
