#  ____  _        _                  
# / ___|| |_ _ __(_)_ __   __ _      
# \___ \| __| '__| | '_ \ / _` |     
#  ___) | |_| |  | | | | | (_| |     
# |____/ \__|_|  |_|_| |_|\__, |     
#                         |___/      
#
# https://docs.python.org/2/library/stdtypes.html#string-methods

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