a,b=0,1
n=int(input("enter number of times"))
print("{}\t{}".format(a,b),end='\t')
n = n-2
while n :
    a,b=b,a+b
    print(b,end='\t')
    n -= 1
