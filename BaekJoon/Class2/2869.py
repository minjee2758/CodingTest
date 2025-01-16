A, B, V = map(int, input().split())

h = (V-B) // (A-B)
if h < (V-B)/(A-B) :
    h += 1
print(h)