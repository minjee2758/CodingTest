L = {}


N = int(input())

for i in range(N) :
    word = input()
    k = len(word)

    if k not in L :
        L[k] = set()
    
    L[k].add(word)

for l in sorted(L.keys()):
      for word in sorted(L[l]) :
            print(word)