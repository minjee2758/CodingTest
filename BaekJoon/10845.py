from collections import deque
import sys

input = sys.stdin.readline
List = deque()
N = int(input())

for i in range(N):
    Command = list(input().split())
    if Command[0] == 'push':
        List.append(Command[1])

    elif Command[0] == 'pop' :
        if len(List) >0 :
            print(List.popleft())
        else : print(-1)
    elif Command[0] == 'size' :
        print(len(List))
    elif Command[0] == 'empty' :
        if len(List) > 0 : 
            print(0)
        else : print(1)
    elif Command[0] == 'front':
        if len(List) > 0 :
            print(List[0])
        else : print(-1)
    elif Command[0] == 'back' :
        if len(List) > 0 :
            print(List[-1])
        else : print(-1)

