M = int(input())
N = int(input())

P=[]

for i in range(M,N+1) :
    error = 0
    if i>1 :
        for j in range(2, i) :
            if i%j==0 :
                error +=1
                break
        if error==0 :
            P.append(i)

if len(P)==0:
    print(-1)
else :
    print(sum(P))
    print(min(P))