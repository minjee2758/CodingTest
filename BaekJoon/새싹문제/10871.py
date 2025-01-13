n, x = map(int, input().split())
a = list(map(int, input().split()))
li = []

for i in a :
    if i <x :
        li.append(i)
    else :
        continue

for i in li :
    print(i, end= ' ')