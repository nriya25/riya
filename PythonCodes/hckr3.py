l=[1,0,-3,-4,3]
z=0
p=0
n=0
k=len(l)
for x in l :
    if x > 0 :
        p =p+1
    if x < 0 :
        n= n+1
    if x == 0 :
        z= z+1
print("p=",p)
print("n=",n)
print("z=",z)
print("positive",p/k)
print("negative",n/k)
print("zero",z/k)

