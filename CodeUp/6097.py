h, w = map(int, input().split())
ar = [[0 for i in range(w)] for j in range(h)]

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if d == 0 :
        for k in range(l):
            if y + k < w:
                ar[x][k+y] = 1
            else:
                break
    else :
        for k in range(l):
            if x + k < h: 
                ar[x+k][y] = 1
            else:
                break

for i in range(h) :
    for j in range(w) :
        print(ar[i][j], end=' ')
    print()