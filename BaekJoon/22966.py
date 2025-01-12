n = int(input())
lowL = 5
lowT = "a"

for i in range(n):
    title, level = input().split()
    level = int(level)
    if level <= lowL :
        lowL = level
        lowT = title

    else :
        continue
print(lowT)