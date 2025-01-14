while True :
    T = list(map(int, input().split()))
    if sum(T) == 0 :
        break
    else :
        T.sort()
        if T[2]**2 == T[0]**2 + T[1]**2 :
            print("right")
        else :
            print("wrong")