from sys import stdin
from threading import Thread


def main():
    n = int(stdin.readline())
    # print(n & 1)
    while n != 1:
        print(n, end=" ")
        if n & 1 == 1:
            n = n * 3 + 1
        else:
            n = n // 2
    print("1", end=" ")


Thread(target=main).start()
