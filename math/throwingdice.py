# nth fibonacci number
from sys import stdin


mod = 1000000007


def getAns(num):
    m = [[0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1]]
    if num == 0:
        return 0
    power(m, num - 1)
    return m[5][5]


def multiply(mat1, mat2):
    temp = [[0] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            for k in range(6):
                temp[i][j] += mat1[i][k] * mat2[k][j]
    for x in range(6):
        for y in range(6):
            mat1[x][y] = temp[x][y]
    print(mat1)


def power(m, p):
    if p == 0 or p == 1:
        return
    tp = [[0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1],
          [0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1]]
    power(m, p // 2)
    multiply(m, m)

    if p % 2:
        multiply(m, tp)


n = int(stdin.readline())
print(getAns(n) % mod)
