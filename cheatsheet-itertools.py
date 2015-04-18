#  ___ _            _              _      
# |_ _| |_ ___ _ __| |_ ___   ___ | |___  
#  | || __/ _ \ '__| __/ _ \ / _ \| / __| 
#  | || ||  __/ |  | || (_) | (_) | \__ \ 
# |___|\__\___|_|   \__\___/ \___/|_|___/ 
# 
# https://docs.python.org/2/library/itertools.html

import itertools

for i in itertools.chain([1, 2, 3], ['a', 'b', 'c']):
    print i
    
for i in itertools.count(5):
    print i
    if i == 20:
        break
    
j = 0    
for i in itertools.cycle([1, 2, 3]):
    j += 1
    print i
    if j == 10:
        break
        

for i in itertools.izip([1, 2, 3], ['a', 'b', 'c']):
    print i

for i in itertools.compress('ABCDEF', [1,0,1,0,1,1]):
    print i
    
for i in itertools.product('AB', 'CD'):
    print i

print '--product'
for i in itertools.product('ABC', repeat=2):
    print i    

print '--permutations'
for i in itertools.permutations('ABC', 2):
    print i    

print '--combinations'    
for i in itertools.combinations('ABC', 2):
    print i        
    
print '--combinations_with_replacement'    
for i in itertools.combinations_with_replacement('ABC', 2):
    print i        