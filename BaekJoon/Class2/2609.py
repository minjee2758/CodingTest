a, b = map(int, input().split())

if a>b :
    k = b
else :
    k = a

L = []

for i in range(1, k+1) :
    if a%i == 0 and b%i==0 :
        L.append(i)

m = max(L)
print(m)
print(m*(a//m)*(b//m))