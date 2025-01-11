r, g, v = map(int, input().split())
for i in range(0, r):
    for j in range(0, g):
        for k in range(0,v):
            print(i, j, k)
print(r*g*v)