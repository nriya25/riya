n=int(input("enter no of rows"))
ch=65
for row in range(0,n) :
    for col in range(0,row+1) :
        c = chr(ch)
        print(c,end='')
    ch += 1
    print()



print("\n\n")

ch=65
row=1
while row <= n :
    col = 1
    while col <= row :
        c=chr(ch)
        print(c,end='')
        col += 1
    ch +=1
    print()
    row += 1


