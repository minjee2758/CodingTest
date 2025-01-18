#백준 11050번 '이항계수1' - Python
#이항계수의 다이나믹 프로그래밍 nCk = n-1Ck + n-1Ck-1
C = [[1]*11 for i in range(11)]

for i in range(1,11) :
    for j in range(1,i) :
            C[i][j] = C[i-1][j] + C[i-1][j-1]


N, K = map(int,input().split())

print(C[N][K])