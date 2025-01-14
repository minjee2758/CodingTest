T = int(input())
for i in range(T) :
    Ys = 0
    Ks = 0
    for j in range(9) :
        Y, K = map(int,input().split())
        if Y >K :
            Ys+=1
        elif Y == K :
            continue
        else :
             Ks+=1
    if Ys > Ks :
        print("Yonsei")
    elif Ys == Ks :
        print("Draw")
    else :
        print("Korea")