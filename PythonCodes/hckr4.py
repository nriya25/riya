l=[1,2,3,4,5]
print(l[1])
s =0
k=[]
i=0
for var in l :
      s = var + s
      print("s=",s)
      i= i+1
    
if i < s :
    s=s-l[i]
    k.append(s)
print(k)

