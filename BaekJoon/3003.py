#킹, 퀸, 룩, 비숍, 나이트, 폰

White = [1, 1, 2, 2, 2, 8]

Now = list(map(int,input().split()))

for i in range(6) :
    print(White[i]-Now[i], end='')