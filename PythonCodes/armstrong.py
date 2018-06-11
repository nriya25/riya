n=int(input("enter a number"))
c=0
num = n
while n > 0 :
    n = n//10
    c = c + 1

n=num
b=0
while n :
    r = n % 10
    n = n // 10
    b = b + r**c
if b == num :
    print("armstrong number")
else :
    print("not armstrong number")
