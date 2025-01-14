n, m, s = map(int, input().split())
c = int(input())

if s+c >=60 :
    m += (s+c)//60
    if m>=60 :
        n += m//60
        print(n%24, m%60, (s+c)%60)
    else :
        print(n, m%60, (s+c)%60)
else :
    print(n, m, s+c)