w, h, b = map(int, input().split())
memory = w*h*b
MB = w*h*b/8/1024/1024
print(format(MB, '.2f'), "MB")