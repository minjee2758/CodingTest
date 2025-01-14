n, m = map(int, input().split())
c = int(input())
if m+c >=60 :
    n += (m+c)//60
    print(n%24, (m+c-60)%60)
else :
    print(n, m+c)