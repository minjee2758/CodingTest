import sys

N = int(input())
L = {}

for i in range(N) :
    word = sys.stdin.readline()
    l = len(word)

    if l not in L :
        L[l] = set()

    L[l].add(word)

for i in sorted(L.keys()):
    for word in sorted(L[i]) :
        print(word)