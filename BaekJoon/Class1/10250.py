T = int(input())
for i in range(T) :
    H, W, N = map(int, input().split())
    floor = N%H
    last = N//H+1
    if floor == 0 :
        floor = H
        last = N//H
        print(H*100+last)
    else :
        print(H*100+last)
