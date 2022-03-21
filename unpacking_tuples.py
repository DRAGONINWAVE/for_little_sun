#eg.1
t = (20,3)
a,b = divmod(*t) # * use the function_divmod
print(a)
print(b)

#eg.2
#os.path.split() function builds a tuple (path,last_part) from a filesystem path
import os
_,filename = os.path.split(r'C:\Users\Administrator\Documents\2021最新社区实习报告范文5篇_社区实习报告范文大全_files\8ea95c379f88094d208b8a7e8afe53fb_lp.jpg')
print(filename)

#eg.3
#using * grab excess items
a,b,*rest = range(7)
print(a,b,rest)
*a,b,rest = range(7)
print(a,b,rest)