s = input()
n = len(s)
res = -1
prev = ""
temp = 0

for i in range(n):
    if s[i] == prev:
        temp += 1
    else:
        temp = 1
    prev = s[i]
    if temp > res:
        res = temp
print(res)
