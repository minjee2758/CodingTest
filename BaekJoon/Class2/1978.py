#1. 몇개인지 입력받기
N = int(input())


#2. 리스트(L)로 수 입력 받기 
L = list(map(int, input().split()))

#3. 총 소수 개수(decimal) 정의
decimal = 0

#4. L안에 있는 숫자를 하나씩 대입하기
for j in L :
    #5. j의 약수의 개수 구하기
    sum = 0
    for k in range(1, j+1) :
        if j%k == 0 :
            sum+=1
    #6. 만약에 약수 개수가 2개면 소수다
    if sum == 2 :
        decimal += 1
print(decimal)
