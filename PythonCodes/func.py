def func(x,y=10,*args,**kwargs):
    """Doc String"""
    print("\npositional argument x=",x)
    print("\nDefault Argument y=",y)
    print("\nVar length argument as tuple:")
    c=1
    for var in args:
        print("var length argument{}:{}".format(c,var))
        c=c+1
    print("\nKey with arguments")
    for key,value in kwargs.items():
        print("{}={}".format(key,value))
        print()
    return "sucess"


print("func(10)",func(10))
print()
print("func(10,20)",func(10,20))
print()
print("var length",func(10,20,'hello','hi',1,2,3,4))
print("dictionary",func(10,name='python',type='programmin language'))
