#분해합의 결과를 N으로 input받기
N = int(input())

#1부터 N까지 수를 하나씩 분해합해보기
for i in range(1, N+1):
    sumN = sum(map(int, str(i)))
    sumNI = sumN + i

	#만약에 i를 분해한 값인 sumNI가 N이랑 같으면 출력
    if sumNI == N :
        print(i)
        break
    #끝까지 찾지 못하면 0 출력
    if i == N :
        print(0)