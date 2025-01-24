# 설탕 배달

N = int(input())

L = []
B = N//5

for i in range(B+1) :
    if (N - 5*i)%3 ==0 :
        a = (N - 5*i)//3
        print("a = ", a, "b = ", i)
        L.append(a+i)

if len(L) ==0 :
    print(-1)
else :
    print(min(L))