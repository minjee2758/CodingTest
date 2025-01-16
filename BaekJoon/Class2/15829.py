L = int(input())
S = input()
total = 0

for i in range(L) :
    num = ord(S[i])-96
    total += num * 31**i

H = total %1234567891
print(H)