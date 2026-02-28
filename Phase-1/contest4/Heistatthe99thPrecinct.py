t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    initial = max(arr)
    count = 0

    for num in arr:
        if num == initial:
            count +=1
    if count%2 == 0:
        print("NO")
    else:
        print("YES")