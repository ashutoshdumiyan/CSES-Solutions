from sys import stdin

# Kadane Algorithm

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]

msf = li[0]
meh = li[0]

for i in range(1, n):
    meh = max(li[i], meh + li[i])
    msf = max(meh, msf)
print(msf)
