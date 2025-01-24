import sys

N = int(input())

#절댓값 주의하기
L = [0 for i in range(2000001)]

for i in range(N) :
    n = int(sys.stdin.readline())+1000000
    L[n] += 1

for i in range(2000001) :
    if i != 0:
        for j in range(L[i]) :
            i -= 1000000
            print(i)