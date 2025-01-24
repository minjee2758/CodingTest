#제로
import sys

K = int(input())
L = []

for i in range(K) :
    n = int(input())
    if n == 0 :
        L.pop()
    else :
        L.append(n)


sumL = sum(L)
print(sumL)