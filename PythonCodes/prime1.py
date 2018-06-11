x=int(input("enter starting value"))
y=int(input("enter ending value"))
if x <= 2:
  print("2",end='\t')
while x <= y :
   c=2
   while c <= x//2 + 1 :
       if x % c == 0 :
          break
       elif c == x//2 +1 :
          print(x,end='\t')
       c=c+1
   x = x + 1
