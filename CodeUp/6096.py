d = [[0 for i in range(19)] for j in range(19)]

for i in range(19) :
    d[i] = list(map(int, input().split()))

count = int(input())
for i in range(count) :
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        for l in range(19) :
            if l == y :
                continue
            elif d[x][l] == 0 :
                d[x][l] = 1
            elif d[x][l] == 1 :
                d[x][l] = 0
        for l in range(19):
            if l == x : 
                continue
            elif d[l][y]==0 :
                d[l][y] =1
            elif d[l][y]==1 :
                d[l][y] ==0
        

for i in range(19) :
    for j in range(19) :
        print(d[i][j], end= ' ')
    print()