num = int(input())
y = 0
n = 0
for i in range(num) :
    op = int(input())
    if op ==0 :
        n += 1
    else :
        y +=1

if y >= n :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")