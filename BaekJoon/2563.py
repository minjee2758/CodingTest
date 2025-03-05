paper = [[0]*100 for i in range(100)]
n = int(input())
maxA = 0
sumPaper =0

for i in range(n):
    a, b = map(int, input().split())
    if a>=maxA :
        maxA = a
    for i in range(a, a+10):
        for j in range(b,b+10):
            paper[i][j] = 1

for i in range(maxA+10):
    sumPaper += paper[i].count(1)
print(sumPaper)