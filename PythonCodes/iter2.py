class PowNum(object):
    def __init__(self,n=2,p=0):
        self.n=n
        self.p=p
    def __iter__(self):
        self.c=0
        return self
    def __next__(self):
        if c <= p:
            self.c +=1
            r = n**c
            return r
        else:
            raise StopIteration


p=PowNum(int(input("Number:")),int(input("Power")))
p=iter(p)
while input("for next value enter something"):
    try:
        
        n=next(p)
        print(n)
    except StopIteration as e:
        print("Error!",e)
        if input():
            main()

