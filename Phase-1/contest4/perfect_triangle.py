t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    initial = arr[1]
    op = 0
    op_arr = []
    for i in range(1, len(arr)-1):
        op = (arr[i] - arr[i-1]) +  (arr[i+1] - arr[i])
        op_arr.append(op)

    print(min(op_arr)) 

    # 6 4 7