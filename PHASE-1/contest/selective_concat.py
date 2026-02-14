t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    limit = n - (k-2)
    found = False
    expected = 1
    count = 0

    for num in a:
        if num == expected:
            count +=1
            expected +=1
            if count == limit:
                break
    print (expected)