# 분수 찾기
X = int(input())

for i in range(1, X) :
    X-=i
    if X<0 :
        if i%2==0 :
            