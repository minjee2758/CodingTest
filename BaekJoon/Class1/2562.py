L = []
for i in range(9):
    k = int(input())
    L.append(k)
print(max(L))
n=0
for i in L :
    n+=1
    if i == max(L) :
        print(n)
        