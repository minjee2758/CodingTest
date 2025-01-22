#덩치
N = int(input())

Data = []
L=[]

for i in range(N) :
    a, b = map(int, input().split())
    Data.append((a,b))

for i in range(N) :
    num = 0
    for j in range(N) :
        if Data[i][0] < Data[j][0] and Data[i][1]<Data[j][1] :
            num += 1    
    L.append(num+1)

for i in L :
    print(i, end = ' ')