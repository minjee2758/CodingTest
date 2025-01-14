N = int(input())

num = map(int, input().split())

max = -1000000
min = 1000000

for i in num :
    if i>=max :
        max = i
    if i <= min :
        min = i

print(min, max)