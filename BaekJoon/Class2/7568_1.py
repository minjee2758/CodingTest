#덩치 문제 다시 풀기
import sys

#전체 사람의 수 N
N = int(input())

#키와 몸무게를 저장할 리스트 선언
L = []
Data = []

for i in range(N) :
    x, y = map(int, input().split())
    L.append((x,y))

for i in range(N):
    num=0
    for j in range(N):
        if L[i][0] < L[j][0] and L[i][1] < L[j][1] :
            num += 1
    Data.append(num+1)

print(Data)