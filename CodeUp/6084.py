h, b, c, s = map(int,input().split())
storage = h*b*c*s
MB = storage/8/1024/1024
print(format(MB, ".1f"), "MB")