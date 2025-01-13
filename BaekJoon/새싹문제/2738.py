n, m = map(int, input().split())
A = []
B = []
for i in range(n) :
    atomA = list(map(int,input().split()))
    A.append(atomA)

for i in range(n) :
    atomB = list(map(int,input().split()))
    B.append(atomB)


print(A)
print(B)

for i in range(n) :
    for j in range(m) :
        print(A[i][j] + B[i][j], end = ' ')
    print()