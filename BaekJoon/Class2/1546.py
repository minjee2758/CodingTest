N =int(input())

S = list(map(int, input().split()))

highS = max(S)

sum=0

for i in range(N) :
    sum += (S[i]/highS)*100

print(sum/N)