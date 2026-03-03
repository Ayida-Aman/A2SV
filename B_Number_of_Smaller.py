n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j= 0
res = []
count = 0
for j in range(len(b)):
    while i < len(a) and a[i] < b[j]  :
        count +=1
        i+=1
    res.append(count)
    j+=1
print(*res)