l=[1,2,3]
k=[5,1,3]
c=0
x=0
for a,b in zip(l,k) :
        print("a=",a)
        print("b=",b)
        if a > b :
            c= c + 1
        if a < b :
            x = x+ 1
        if a == b :
            pass
print("c=",c)
print("x=",x)
