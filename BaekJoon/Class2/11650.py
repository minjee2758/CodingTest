#좌표 정렬하기
import sys

N = int(input())
L = []

for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    L.append((x,y))

L.sort()

sys.stdout.write("\n".join(f"{x} {y}" for x, y in L))