S = input()
n = len(S)

for i in range(n) :
    k = S[i]
    if ord(k) <=90 :
        s = ord(k)-32
        print(chr(s), end='')
    else :
        s = ord(k) + 32
        print(chr(s), end='')