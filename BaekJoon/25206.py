S = {"A+" : 4.5, "A0" : 4.0,
     "B+" : 3.5, "B0" : 3.0,
     "C+" : 2.5, "C0" : 2.0,
     "D+" : 1.5, "D0" : 1.0,
     "F" : 0.0}
total_score=0
n=0
for i in range(20) :
    subject, point, score = input().split()
    if score !="P" :
        total_score += float(point) * float(S[score])
        n+=float(point)

print("%.6f" %(total_score/n))