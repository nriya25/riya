l=[1234556,34567,1234566,76554]
from functools import reduce
k=reduce(lambda x,y :x+y,l)
print(k)
