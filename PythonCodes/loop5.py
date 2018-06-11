data=[]
while input("type something") :
    d=input("enter key-value pair").split('=')
    data.append(d)
    mylist=dict(data)
print(mylist)    
