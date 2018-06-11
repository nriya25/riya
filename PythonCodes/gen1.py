def Pow(n,p):
    c=0
    while c <= p:
        k = n**c
        c +=1
        yield k
    else :
        raise StopIteration

