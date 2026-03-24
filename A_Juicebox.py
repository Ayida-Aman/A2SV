from collections import Counter


t = int(input())

for _ in range(t):
    n, k = map(int, input())
    b = []
    c = []
    for i in range(k):
        bi = int(input())
        ci = int(input())
        b.append(bi)
        c.append(ci)
    if len(list(set(b))) <= n:
        print(sum(c))
    else:
        