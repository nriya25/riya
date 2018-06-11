s='saveChangesInTheEditor'
"""print(s.istitle())
for var in s:
    k=str(var.istitle())
    print("{}={}".format(var,k))
    if k == 'True':
"""

k = ''
for ch in s :
    if ch.isupper() :
        k += ','+ch
    else :
        k += ch
l=list(k.split(','))
print(l)
c=0
for key in l:
    c=c+1
print(c)
    
        
        

