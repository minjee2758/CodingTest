n = int(input())
a = list(map(int, input().split()))
same = int(input())
num = 0

for i in a :
    if i == same :
        num+=1
    else :
        continue

print(num)