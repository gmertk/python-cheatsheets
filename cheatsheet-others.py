#  ____        _ _ _       ___        
# | __ ) _   _(_) | |_    |_ _|_ __   
# |  _ \| | | | | | __|____| || '_ \  
# | |_) | |_| | | | ||_____| || | | | 
# |____/ \__,_|_|_|\__|   |___|_| |_| 
#                                     

print '\n-- built-in'
# divmod(x, y) -> (x/y, x%y)	
a, b = divmod(5, 3)
print 'divmod(5, 3) = (' + str(a) + ', ' + str(b) + ')'

# hex(integer) -> str: hexadecimal representation of integer number
a = hex(15)
print 'hex(15) = "' + str(a) + '"'



# __  __       _   _           
# |  \/  | __ _| |_| |__        
# | |\/| |/ _` | __| '_ \       
# | |  | | (_| | |_| | | |      
# |_|  |_|\__,_|\__|_| |_|      
# 
                            
import math
print '\n-- math module'

# ceil(x) -> float: smallest integral value >= x
a = math.ceil(4.1)
print 'math.ceil(4.1) = ' + str(a)

# floor(x) -> float: largest integral value <= x
a = math.floor(4.1)
print 'math.floor(4.1) = ' + str(a)

# pow(x,y) -> float: x raised to y power (xy)
a = math.pow(2, 3)
print 'math.pow(2, 3) = ' + str(a)



# ____                 _                 
# |  _ \ __ _ _ __   __| | ___  _ __ ___  
# | |_) / _` | '_ \ / _` |/ _ \| '_ ` _ \ 
# |  _ < (_| | | | | (_| | (_) | | | | | |
# |_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_|
#
                        
import random
print '\n-- random module'

# random() -> float: random value in [0.0, 1.0[
a = random.random()
print 'random.random() = ' + str(a)

# randint(a,b) -> int: random value in [a, b]
a = random.randint(0, 5)
print 'random.randint[0, 5] = ' + str(a)

# uniform(a, b) -> float: random value in [a, b[
a = random.uniform(0, 5)
print 'random.uniform[0, 5[ = ' + str(a)

# randrange([start,]stop[,step]) -> int: random value in range(start, stop, step)
a = random.randrange(0, 10, 3)
print 'random.randrange(0, 10, 3) = ' + str(a)

# choice(seq) -> value: random item from seq sequence
a = random.choice(["mert", "gunay", "kth"])
print 'random.choice(["mert", "gunay", "kth"]) = ' + str(a)

# sample(population,k) -> list: k random items from polulation
a = random.sample(["mert", "gunay", "kth", "stockholm"], 2)
print 'random.sample(["mert", "gunay", "kth", "stockholm"], 2) = ' + str(a)

a = [1, 2, 3, 4]
random.shuffle(a)
print a

# ____  _ _     _                   _   
# | __ )(_) |_  | |    _____   _____| |  
# |  _ \| | __| | |   / _ \ \ / / _ \ |  
# | |_) | | |_  | |__|  __/\ V /  __/ |  
# |____/|_|\__| |_____\___| \_/ \___|_|  
#
 
print '\n-- bit level operations'

# ~x -> inverted bits of x
a = ~3
print '~3 = ' + str(a)

# x<<n -> x shifted left by n bits (zeroes inserted)
a = 1 << 1
print '1 << 1 = ' + str(a)

# x>>n -> x shifted right by n bits (zeroes inserted)
a = 1 >> 1
print '1 >> 1 = ' + str(a)



#  ____  _        _                  
# / ___|| |_ _ __(_)_ __   __ _      
# \___ \| __| '__| | '_ \ / _` |     
#  ___) | |_| |  | | | | | (_| |     
# |____/ \__|_|  |_|_| |_|\__, |     
#                         |___/      

print '\n-- string operations'

# chr(code) -> str: string of one char
a = chr(65)
print 'chr(65) = "' + a + '"'

# ord(char) -> int: code
a = ord('A')
print 'ord("A") = ' + str(a)

# str(expr) -> str: readable textual representation of expr - if available
a = str(123)
print 'str(123) = "' + a + '"'

# len(s) -> int: number of chars in the string
a = len('mert')
print 'len("mert") = ' + str(a) 

# s.capitalize() -> string with first char capitalized
a = 'mert'.capitalize()
print '"mert".capitalize() = ' + str(a) 

# s.center(width[,fillchar]) -> string centered 
a = 'mert'.center(8, '$')
print '"mert".center(8, "$") = ' + str(a) 

# s.count(sub[,start[,end]]) -> int: count sub occurences
a = 'mererter'.count('er')
print '"mererter".count("er") = ' + str(a) 

# s.find(sub[,start[,end]]) -> int/-1: offset of sub
a = 'merte'.find('e')
print '"merte".find("e") = ' + str(a) 

# s.rfind(sub[,start[,end]]) -> int/-1: last offset of sub
a = 'merte'.rfind('e')
print '"merte".rfind("e") = ' + str(a) 

# s.rsplit([sep[,maxsplit]]) -> [string]: rightmost words delim. by sep
a = 'merte'.rsplit('e', 1)
print '"merte".rsplit("e", 1) = ' + str(a) 

# s.split([sep[,maxsplit]]) -> [string]: rightmost words delim. by sep
a = 'merte'.split('e', 1)
print '"merte".split("e", 1) = ' + str(a) 

# s.endswith(suffix[,start[,end]]) -> bool: test text ending
a = 'mert'.endswith('rt')
print '"mert".endswith("rt") = ' + str(a) 

# s.startswith(suffix[,start[,end]]) -> bool: test text begining->
a = 'mert'.startswith('m')
print '"mert".startswith("m") = ' + str(a) 

# s.strip([chars]) -> string text with leading+trailing chars removed
a = 'mertddeeeddeeeefff'.strip('fed')
print '"mertddeeeddeeeefff".strip("fed") = ' + str(a)