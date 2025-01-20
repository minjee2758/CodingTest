n1 = input()
n2 = input()
n3 = input()

L = []
L.append(n1)
L.append(n2)
L.append(n3)
P = []
N =[]

for i in range(3) :
    if L[i] == "Fizz" :
        L[i] = 3
    elif L[i] == "Buzz" :
        L[i] = 5
    elif L[i] =="FizzBuzz" :
        L[i] = 15
    else :
        L[i] = int(L[i])
        P.append(L[i])
        N.append(i)

if N[0] ==0 :
    k = P[0] + 3
elif N[0] == 1 :
    k = P[0] + 2
else :
    k = P[0] + 1

if k %3 ==0 :
    if k%5==0 :
        print("FizzBuzz")
    else :
        print("Fizz")
elif k%5 ==0:
    print("Buzz")
else :
    print(k)