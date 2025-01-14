n = input()
long = len(n)
h = 10

for i in range(1, long):
    if n[i-1] ==n[i]:
        h+=5
    else :
        h +=10

print(h)