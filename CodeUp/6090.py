a, m, d, n = map(int, input().split())
sequence = a
for i in range(n-1) :
    sequence = sequence*m+d

print(sequence)
