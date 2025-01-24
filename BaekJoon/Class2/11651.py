#좌표 정렬하기 2

import sys

N = int(input())
L = []

for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    L.append((y,x))

L.sort()

sys.stdout.write("\n".join(f"{x} {y}" for y, x in L))