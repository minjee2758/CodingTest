S = list(input())
L=[]
for i in range(26) :
    L.append(-1)

for j in range(len(S)) :
    if L[ord(S[j])-97] ==-1 :
        L[ord(S[j])-97] = j

for k in range(26) :
    print(L[k], end=' ')