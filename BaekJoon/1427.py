#방법 1
# N = int(input())
# L= []
# while True :
#     if N<10 :
#         break
#     else :
#         L.append(N%10)
#         N = (N- N%10)//10
# L.append(N)
# L.sort()
# L.reverse()
# for i in L :
#     print(i, end="")

#방법2
N = int(input())
L = []
for i in str(N) :
    L.append(int(i))
L.sort()
L.reverse()
for i in L :
    print(i, end="")