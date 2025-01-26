#단어 공부

word = input()
L=[0 for i in range(26)]
for i in word :
    n = ord(i)
    if n>=97 :
        n -= 32
    L[n-65] += 1
P = []
for i in range(26) :
    if L[i] == max(L) :
        P.append(i)

if len(P)>1 :
    print("?")
else :
    print(chr(P[0]+65))