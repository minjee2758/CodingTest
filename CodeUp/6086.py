n = int(input())
sum = 0
while sum <n :
    for i in range(1, n+1) :
        if sum >=n :
            break
        else :
            sum +=i
print(sum)