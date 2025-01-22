#나이순 정렬
#https://www.acmicpc.net/problem/10814
import sys
N = int(input())
Data = []
L=[]

for i in range(N) :
    a, b = sys.stdin.readline().strip().split()
    Data.append((i, int(a),b))

Data.sort(key=lambda x : (x[1], x[0]))

for i, age, name in Data :
    print(age, name)