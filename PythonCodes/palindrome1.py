n=int(input("enter a number"))
s=0
temp=n
while n > 0 :
    r = n % 10
    n = n // 10
    s=s*10 +r
if s==temp :
    print("palindrome")
else :
    print("not palindrome")
