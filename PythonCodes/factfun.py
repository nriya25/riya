def fact(num) :
  if num >= 0 : 
     if num :  
        i=1
        fact=1
        while i<= num :
            fact = fact * i
            i=i+1
        return fact
     else :
        return 1
  else :
      print("negative number")


x=int(input("enter number for factorial"))
f=fact(x)
print(f)
