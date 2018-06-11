x=int(input("enter a number"))
a,b=0,1
print("{}\t{}".format(a,b),end='\t')

while b <= x :
    a,b=b,a+b
    if b >= x :
        break
    print(b,end='\t')
