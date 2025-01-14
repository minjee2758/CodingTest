S = input().split(" ")
l = len(S)
if S[-1] == "" :
    l -=1
elif S[0] =="":
    l -= 1
print(l)