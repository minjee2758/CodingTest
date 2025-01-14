S = int(input())
result = 0
sum = 0 

for i in range(1, S+1):
    result += 1
    sum += i
    if sum > S :
        result -= 1
        break

print(result)
