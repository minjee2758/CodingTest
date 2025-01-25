# 카드210
import math
N = int(input())

k = int(math.log2(N))
maxK = 2**k


l = N-maxK

if N ==1 :
    print(1)
else :
    print(2*l)