#덩치
N = int(input())

L = [[]*2 for i in range(N)]
print(L[0][1])
for i in range(N) :
    p, q = map(int, input().split())
    L[i].append