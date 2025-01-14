n = int(input())
a = b = 100
for i in range(n) :
    A, B = map(int,input().split())
    if A == B :
        continue
    if A>B :
        b -= A
    else :
        a -= B
print(a, b)