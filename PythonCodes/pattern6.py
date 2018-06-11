n=int(input("enter no of rows"))
for row in range(1,n+1) :
    c=65
    for col in range(1,row+1) :
        print(chr(c),end='')
        c=c+1
    print()


print("\n\n")

row=1
while row <= n :
    col = 1
    c=65
    while col <= row :
        print(chr(c),end='')
        c += 1
        col += 1
    print()
    row += 1
             



