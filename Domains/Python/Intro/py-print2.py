"""Not an original idea but a very pythonic solution!!
print(*objects, sep=' ', end='\n', file=sys.stdout) is not normally available 
as a built-in since the name print is recognized as the print statement. To disable 
the statement and use the print() function, use the future statement at the top of your module
"""
# To Learn more, Check Python2.7 and 3.5 Documentations.
# The following code works for both Py2.7 and 3.5

from __future__ import print_function

print(*range(1, int(input())+1), sep='')
