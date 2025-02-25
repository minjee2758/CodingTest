#세로 읽기
words = []
max = 0
for i in range(5):
    l = input()
    if len(l) >= max :
        max = len(l)
    words.append(l)

for i in range(max):
    for j in range(5) :
        if len(words[j])>i :
            print(words[j][i], end='')