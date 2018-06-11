student={'name':[],
         'addr':[],
         'class':[],
         'phone':[]}
while input("enter something to continue") :
    n=input("enter students name")
    student['name'].append(n)
    ad=input("enter address")
    student['addr'].append(ad)
    cl=input("enter class")
    student['class'].append(cl)
    p=input("enter number")
    student['phone'].append(p)

print(len(student['name']))
c=0
while c < len(student['name']) :
    print("name=",student['name'][c])
    print("address=",student['addr'][c])
    print("class=",student['class'][c])
    print("number=",student['phone'][c])
    print("\n\n")
    c=c + 1

