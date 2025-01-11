n = int(input())
a = list(map(int, input().split()))

k = a[0]
for i in range(1, n):
    if k>=a[i] :
        k = a[i]
print(k)