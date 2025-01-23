N, M = map(int, input().split())

cards = list(map(int, input().split()))
P = []

for i in range(N) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            if k<N+1 :
                sum = cards[i] + cards[j] + cards[k]
                if sum<=M :
                    P.append(sum)

print(max(P))