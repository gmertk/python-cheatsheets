#  ____       _                          
# / ___|  ___| |_ ___                    
# \___ \ / _ \ __/ __|                   
#  ___) |  __/ |_\__ \                   
# |____/ \___|\__|___/                   
# 
# https://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset

s = set([1, 2, 2, 3, 3])
frozenSet = frozenset([1, 2, 2, 3, 3])
#frozenSet.add(4) gives error

print s
print s.issubset([1, 2, 2])
print s.issuperset([1, 2, 2])
s.add(2)
s.add(4)
print s
s.remove(2)
# s.remove(5) # Raise KeyError since 5 is not in the set
print s
s.clear()
print s
s.add(1)
s.add(2)

print s.intersection([1, 2, 6, 7])
print s & set([1, 2, 6, 7])

print s.union([6])
print s | set([6])

# [x / x is in s and x is not in others]
print s.difference([2])
print s - set([2])

# [x / x is in s xor x is in others]
print s.symmetric_difference([1, 2, 3, 4])
print s ^ set([1, 2, 3, 4])

s.update([5, 6, 7, 8, 1])
print s

if 2 in s:
    print '2 is in s'
    
