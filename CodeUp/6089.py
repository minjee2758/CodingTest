a, r, n = map(int, input().split())
sequence = a
for i in range(n-1) :
    sequence *= r

print(sequence)
