import math

N = int(input())

fac = str(math.factorial(N))

n = 0
for i in range(len(fac)-1, -1, -1) :
    if fac[i] != "0" :
        print(n)
        break
    n+=1