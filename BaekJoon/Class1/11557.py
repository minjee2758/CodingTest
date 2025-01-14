T = int(input())

for i in range(T) :
    max = 0
    mS = ""
    N = int(input())
    for j in range(N) :
        S, L = input().split()
        L = int(L)
        if L>max:
            max = L
            mS = S
    print(mS)
            

