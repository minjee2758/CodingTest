n = int(input())
k=[]

for i in range(n) :
    a, b, c = map(int, input().split())
    if a==b==c :
        k.append(10000+a*1000)
    elif a==b or a==c :
        k.append(1000+a*100)
    elif b==c :
        k.append(1000+b*100)
    else :
        k.append(max(a,b,c)*100)

M = max(k)
print(M)