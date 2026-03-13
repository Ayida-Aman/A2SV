n, s = map(int, input().split())
arr = list (map(int, input().split()))
l = 0
count =total = 0
for i in range(len(arr)):
    total+=arr[i]
    while total > s:
        total-=arr[l]
        l+=1
    count = max(count, i-l+1)
print( count)