while (True) :
    F = list(input())
    if int(F[0]) ==0 :
        break
    n = len(F)
    K = []
    for i in range(n-1, -1, -1) :
        K.append(F[i])

    if F == K :
        print("yes")
    else :
        print("no")