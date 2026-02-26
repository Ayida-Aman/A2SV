t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    possible = True
    for i in range(1, n):
        if arr[i] - arr[i-1] > 1:
            possible = False
            break
    print("YES" if possible else "NO")
