
while True :
    n = int(input())
    if n ==-1 :
        break
    else :
        L =[]
        for i in range(1, n) :
            if n%i==0 :
                L.append(i)

        if sum(L) != n :
            print("{} is NOT perfect".format(n))
        else :
            print("{} = ".format(n), end="")
            print(" + ".join(map(str, L)))
