t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    
    if n == k:
        for i in range(len(a)):
            if (i+1) % 2 == 0:
                b.append(a[i])
        b.append(0)
        
        res = -1
        for i in range(len(b)):
            if (i+1) != b[i]:
                res = i+1
                break
        if res == -1:
            res = (k // 2) + 1
        print(res)
    
    else:
        size = n - k + 2   
        isOne = True
        for i in range(1, size):  
            if a[i] != 1:
                isOne = False
                break
        if isOne:
            print(2)
        else:
            print(1)
