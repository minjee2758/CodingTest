A = int(input())
B = int(input())
C = int(input())

D = str(A*B*C)
L=[]
for i in range(10) :
    L.append(0)

for i in D :
    for j in range(10):
        if int(i) == j :
            L[j] += 1

for i in L :
    print(i)