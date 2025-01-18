T = int(input())
#peopleApartment
pA = [[0]*15 for i in range(15)]

for i in range(1, 15) :
    pA[0][i] = i

for k in range(1,15) :
    for n in range(1,15) :
        pA[k][n] = pA[k-1][n] + pA[k][n-1]

for i in range(T) :
    k = int(input())
    n = int(input())
    print(pA[k][n])