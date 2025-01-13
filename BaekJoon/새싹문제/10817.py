import statistics

num = list(map(int, input().split()))

num.sort()
print(statistics.median(num))