T = int(input())
for i in range(T) :
    R, S = input().split()
    R = int(R)

    for s in range(len(S)) :
        for r in range(R) :
            print(S[s], end='')
    print()