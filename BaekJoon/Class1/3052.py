L = []
for i in range(10) :
    n = int(input())
    last = n%42
    if last not in L :
        L.append(last)

print(len(L))