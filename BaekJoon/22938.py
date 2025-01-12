x1, y1, R1 = map(int, input().split())
x2, y2, R2 = map(int, input().split())

w = (x1-x2)*(x1-x2)
h = (y1-y2)*(y1-y2)

sumR = (R1+R2)**2

if w+h <sumR :
    print("YES")
else :
    print("NO")