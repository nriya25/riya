n=int(input("enter no. of rows"))
m=int(input("enter no of columns"))
l=[]
for row in range(n):
    k=[]
    for col in range(m):
        x=int(input())
        k.append(x)
    l.append(k)
print(l)
print("your matrix is")
for var in l:
     print("\t\t",*var)
i = 0
for i in range(m):
    print(l[-1][i],end=" ")
    print(l[-2][i])
    

            
