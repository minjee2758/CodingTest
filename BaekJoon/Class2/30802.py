#1. 몇 명(N)인지 입력 받기
N = int(input())

#2. 티셔츠 사이즈(TSize)별로 신청한 갯수를 리스트 형태로 받기
TSize= list(map(int, input().split()))

#3. 티셔츠와 펜을 몇묶음씩 사야하는지
T, P = map(int, input().split())

#4. 티셔츠 총 개수 정의
T_sum = 0

#5. 필요한 티셔츠 개수 구하기 - 티셔츠 사이즈 종류만큼 반복 (6회)
for i in range(6) :
	#6. 사이즈별로 0개일 수 있으니 그 경우 제외
    if TSize !=0 :
    	#7. 만약 사이즈별 필요한 개수가 묶음 수로 나누어 떨어지면 몫을 합하고, 나머지가 남으면 몫+1
        if TSize[i]%T!=0 :
            T_sum = T_sum + TSize[i]//T +1
        else :
            T_sum += TSize[i]//T
        
#8. 펜 묶음 수와 낱개로 사야하는 펜수 계산
Pen = N//P
Pen_ = N%P

print(T_sum)
print(Pen, Pen_)