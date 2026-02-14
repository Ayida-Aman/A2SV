t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)

    if total%n != 0:
        print(-1)
        continue
    target = total // n
    k = 0
    for num in arr:
        if num > target:
            k+=1
    print (k)