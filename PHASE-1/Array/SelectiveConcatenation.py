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
        for i in range(len(b)):
            if i+1 != b[i]:
                print(i+1)
                break
    else:
        size = n - (k// 2) 
        if all(x == 1 for x in a[:size]): 
            print(2) 
        else: 
            print(1)




















    # size = n//k
    # b = [a[i*size:(i+1)*size] for i in range(k-1)] 
    # b.append(a[(k-1)*size:])
    # print(b)
    # res = []
    # for i in range(len(b)):
    #     if (i+1) %2 == 0:
    #         for j in range(len(b[i])):
    #             res.append(b[i][j])
    # res.append(0)
    # print(res)
    # for i in range(len(res)):
    #     if i+1 != res[i]:
    #         print(i+1)
    #         break
            