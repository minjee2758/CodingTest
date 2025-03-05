#3 23 85 34 17 74 25 52 65
List = []
Location = [0 for i in range(9)]
for i in range(9) :
    maxN = 0
    N = list(map(int, input().split()))
    for j in range(9):
        if N[j] >= maxN :
            maxN = N[j]
            Location[i]=j
    List.append(maxN)
maxL = 0
a,b =0,0

for i in range(9) :
    if List[i] >= maxL :
        maxL = List[i]
        a, b = i, Location[i]
print(maxL)
print(a+1,b+1)