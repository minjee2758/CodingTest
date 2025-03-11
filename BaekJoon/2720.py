#세탁소 사장 동혁
Q = 25
D = 10
N = 5
P = 1

T = int(input())

for i in range(T) :
    Money = int(input())
    print(Money//Q, end=" ")
    print((Money%Q)//D, end=" ")
    print(((Money%Q)%D)//N, end=" ")
    print((((Money%Q)%D)%N)//P, end=" ")
    print()

n = int(input())

for i in range(n):
	money = int(input())
	for j in [25, 10, 5, 1]:
		print(money//j, end=' ')
		money = money%j