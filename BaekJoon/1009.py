T = int(input())
L = [[10], [1], [2,4,8,6], [3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]

for i in range(T) :
    a, b = map(int, input().split())
    A = a%10
    List = L[A]
    index = (b-1)%len(List)
    print(List[index])
