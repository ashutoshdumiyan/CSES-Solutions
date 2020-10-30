from itertools import permutations

s = input()
li = list(set(permutations(s)))
for i in range(len(li)):
    li[i] = "".join(li[i])
li.sort()
print(len(li))
for o in li:
    print(o)
