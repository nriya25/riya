x=int(input("enter x"))
y=int(input("enter y"))
z=int(input("enter z"))
w=int(input("enter w"))

if x >=y and x >= z :
    if x >=w :
      print("x is greatest")
    else :
      print("w is greatest")
elif y >= x and y >= z :
    if y >= w :
        print("y is greatest")
    else :
        print("w is greatest")
elif z >= x and z >=y :
    if z >= w :
        print("z is greatest")
    else :
        print("w is greatest")
else :
   print(" w is greatest")
