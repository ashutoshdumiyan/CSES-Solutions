from sys import stdin
from collections import deque

n = int(stdin.readline())
sm = (n * (n + 1)) // 2
if sm & 1 == 1:
    print("NO")
else:
    s = sm // 2
    li = deque([_ for _ in range(1, n + 1)])
    fl = 1
    res = 0
    lst = deque()
    while res < s:
        if fl:
            tmp = li.pop()
            lst.append(tmp)
            res += tmp
            fl = 0
        else:
            tmp = li.popleft()
            lst.append(tmp)
            res += tmp
            fl = 1
    print("YES")
    print(len(lst))
    print(*lst, end=" ")
    print(len(li))
    print(*li)
