import sys

N = int(input())

L = [0] * 2000001
offset = 1000000

for i in range(N) :
    a = int(sys.stdin.readline())
    L[a+offset] += 1

for i in range(2000001) :
    if L[i] >0 :
        for j in range(L[i]):
            print(i-offset)