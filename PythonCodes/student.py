student={'name':[],
         'addr':[],
         'class':[],
         'phone':[]}
c=0
while input("enter something to continue") :
    n=input("enter students name")
    student['name'].append(n)
    ad=input("enter address")
    student['addr'].append(ad)
    cl=input("enter class")
    student['class'].append(cl)
    p=input("enter number")
    student['phone'].append(p)
print(student)
print(student.items())
key=student.keys()
value=student.values()
for key,value in zip(key,value) :
    print("{}={}".format(key,value))
print(len(student))
while c <= len(student.values()) -1 :
    print("name=",student['name'][c])
    print("address=",student['addr'][c])
    print("class=",student['class'][c])
    print("number=",student['phone'][c])
    print("\n\n")
    c=c + 1

