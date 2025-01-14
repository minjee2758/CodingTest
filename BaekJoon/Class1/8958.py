T = int(input())

for i in range(T) :
    S = list(input())
    score = 0
    final_score = 0
    for i in S :
        if i == "O" :
            score += 1
            final_score += score
        else :
            score=0
    print(final_score)
