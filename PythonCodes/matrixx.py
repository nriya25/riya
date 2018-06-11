n,m=map(int,input("Enter matrix dimensions").lower().split( ))
def show(X):
    for var in X:
        print("\t",*var)
def trans(X):
    r=[]
    r=[[X[j][i] for j in range(n)] for i in range(m)]
    print("\n")
    for var in r:
        print(var)

def add(X,Y):
    k=[]
    for row in range(n):
        p=[]
        for col in range(m):
            p.append(X[row][col]+Y[row][col])
        k.append(p)
    for var in k:
        print(*var)

print("input matrix A")
A=[list(map(int,input('\t').split())) for var in range (n)]
print("input matrix B")
B=[list(map(int,input('\t').split())) for var in range (n)]
print("matrix A is :")
show(A)
print("matrix B is :")
show(B)

print("\ntranspose of matrix A is")
trans(A)
print("\n transpose of matrix B is")
trans(B)
print("\nsum of matrices is")
add(A,B)


