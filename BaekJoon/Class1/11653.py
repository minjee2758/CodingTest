N = int(input())
L = []
for i in range(2, N) :
    while N%i ==0:
        N = N//i
        L.append(i)

if len(L) ==0 :
    if N != 1 :
        print(N)
else :
    for i in L :
        print(i)
