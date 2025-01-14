A = [1, 2, 3, 4, 5, 6, 7, 8]
D = [8, 7, 6, 5, 4, 3, 2, 1]

S = list(map(int, input().split()))

if S == A :
    print("ascending")
elif S == D :
    print("descending")
else :
    print("mixed")