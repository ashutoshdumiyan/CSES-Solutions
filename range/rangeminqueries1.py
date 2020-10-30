from sys import stdin, maxsize
# li = [0] * 1000000001  # Our array
# st = [0] * 4000000001  # Our Segment Tree

# Segment tree array is indexed 1 based


def build(li, st, si, ss, se):
    # si = segment index
    # ss = segment start
    # se = segment end
    if ss == se:
        st[si] = li[ss]
        return

    mid = (ss + se) // 2
    build(li, st, 2 * si, ss, mid)
    build(li, st, 2 * si + 1, mid + 1, se)
    st[si] = min(st[2 * si], st[2 * si + 1])


def query(st, si, ss, se, qs, qe):
    # qs = query start
    # qe = query end
    if ss > qe or se < qs:
        return maxsize  # Completely out of the segment and doesn't contribute to the solution

    if ss >= qs and se <= qe:
        return st[si]   # Lies completely in the segment
    mid = (ss + se) // 2
    # Return minimum from left and right subtree
    return min(query(st, 2 * si, ss, mid, qs, qe), query(st, 2 * si + 1, mid + 1, se, qs, qe))


def main():
    n, q = map(int, stdin.readline().split())
    li = [0] * (n + 1)
    st = [0] * (4 * (n + 1))
    c = 1
    for i in stdin.readline().split():
        li[c] = int(i)
        c += 1
    build(li, st, 1, 1, n)
    while q:
        a, b = map(int, stdin.readline().split())
        print(query(st, 1, 1, n, a, b))
        q -= 1


if __name__ == "__main__":
    main()
