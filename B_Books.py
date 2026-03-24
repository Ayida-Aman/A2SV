n , k = map(int, input().split())

arr = list(map(int, input().split()))

# arr.sort()
left = total = 0
count = 0

for right in range(n):
    total += arr[right]

    while total > k:
        total -= arr[left]
        left+=1
    count = max(count, right-left+1)
    
print(count)