n=int(input("enter no of rows"))
for row in range(1,n+1) :
    for col in range(1,row+1) :
        print(col,end='')
    print()


print("\n\n")





row =1
while row <= n :
    col = 1
    while col <= row :
        print(col,end='')
        col += 1
    print()
    row += 1
