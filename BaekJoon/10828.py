
import sys

input = sys.stdin.readline

N = int(input())
List = [0 for i in range(N)]
top = -1

for i in range(N):
    Commands = list(input().split())
    command = Commands[0]

    if command == 'push' :
        top +=1
        List[top] = Commands[1]
        print(List)
    elif command == 'pop' :
        if top ==-1 :
            print(-1)
        else :
            print(List[top])
            top -= 1
    elif command == "size" :
        print(top+1)
    elif command == "empty" :
        if top ==-1 :
            print(1)
        else :
            print(0)
    elif command == "top" :
        if top == -1 :
            print(-1)
        else :
            print(List[top])