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
print a  # A

# ord(char) -> int: code
a = ord('A')
print a  # 65

# str(expr) -> str: readable textual representation of expr - if available
a = str(123)
print a  # 123

# len(s) -> int: number of chars in the string
a = len('mert')
print a  # 4

# s.capitalize() -> string with first char capitalized
a = 'mert'.capitalize()
print a  # Mert

# s.center(width[,fillchar]) -> string centered 
a = 'mert'.center(8, '$')
print a  # $$mert$$

# s.count(sub[,start[,end]]) -> int: count sub occurences
a = 'mererter'.count('er')
print a  # 3

# s.find(sub[,start[,end]]) -> int/-1: offset of sub
a = 'merte'.find('e')
print a  # 1

# s.rfind(sub[,start[,end]]) -> int/-1: last offset of sub
a = 'merte'.rfind('e')
print a  # 4

# s.rsplit([sep[,maxsplit]]) -> [string]: rightmost words delim. by sep
a = 'merte'.rsplit('e', 1)
print a  # ['mert', '']

# s.split([sep[,maxsplit]]) -> [string]: rightmost words delim. by sep
a = 'merte'.split('e', 1)
print a  # ['m', 'rte']

# s.endswith(suffix[,start[,end]]) -> bool: test text ending
a = 'mert'.endswith('rt')
print a  # True

# s.startswith(suffix[,start[,end]]) -> bool: test text begining
a = 'mert'.startswith('m')
print a  # True

# s.strip([chars]) -> string text with leading+trailing chars removed
a = 'mertddeeeddeeeefff'.strip('fed')
print a  # mert

# s.replace(s, old, new[, maxreplace])
a = ' hello   mert '.replace(' ', '')
print a # 'hellomert'
