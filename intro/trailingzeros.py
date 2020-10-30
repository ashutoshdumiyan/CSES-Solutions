from sys import stdin

n = int(stdin.readline())

cnt = 0

i = 5
while n / i >= 1:
    cnt += n // i
    i *= 5

print(cnt)
