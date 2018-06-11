
while input("enter something to continue") :
  num=int(input("enter a number"))
  i=2
  while i <= num-1 :
     if num % i == 0 :
         print("not prime")
         break
     elif i == num-1 :
         print("prime")
     i=i+1
