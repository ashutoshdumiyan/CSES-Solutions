from sys import stdin

n = int(stdin.readline())
if n == 1:
    print("1")
elif n < 4:
    print("NO SOLUTION")
else:
    temp = 2
    while temp <= n:
        print(temp, end=" ")
        temp += 2
    temp = 1
    while temp <= n:
        print(temp, end=" ")
        temp += 2
