# nth fibonacci number
from sys import stdin


mod = 1000000007


def getAns(num):
    m = [[1, 1], [1, 0]]
    if num == 0:
        return 0
    power(m, num - 1)
    return m[0][0]


def multiply(mat1, mat2):
    a = (mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % mod
    b = (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % mod
    c = (mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % mod
    d = (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % mod

    mat1[0][0] = a
    mat1[0][1] = b
    mat1[1][0] = c
    mat1[1][1] = d


def power(m, p):
    if p == 0 or p == 1:
        return
    temp = [[1, 1], [1, 0]]
    power(m, p // 2)
    multiply(m, m)

    if p % 2:
        multiply(m, temp)


n = int(stdin.readline())
print(getAns(n) % mod)
