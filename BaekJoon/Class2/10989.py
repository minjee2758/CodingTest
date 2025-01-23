#백준 10989번 '	수 정렬하기 3' - Python
import sys
N = int(sys.stdin.readline())

L = [0]*10000

for i in range(N):
	a = int(sys.stdin.readline())
	L[a-1] += 1

for k in range(10000):
	if L[k] != 0:
		for j in range(L[k]):
			print(k+1)