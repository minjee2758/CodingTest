Cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
n=0
l = 0
for i in Cro :
    if i in word :
        word = word.replace(i, "1")
print(len(word))