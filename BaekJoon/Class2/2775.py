T = int(input())
p=0
for i in range(T) :
    k = int(input())
    n = int(input())    
    for j in range(k) :
        p += (k-1)*n + n
    print(p)