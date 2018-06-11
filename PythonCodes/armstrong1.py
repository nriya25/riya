x=int(input("enter starting range"))
y=int(input("enter ending range"))
while x <= y: 
      n = x
      while n > 0 :
          n = n//10
          c = c + 1

      b=0
      while n :
          r = n % 10
          n = n // 10
          b = b + r**c
      if b == num :
         print("armstrong number=",n)
      x = x + 1
