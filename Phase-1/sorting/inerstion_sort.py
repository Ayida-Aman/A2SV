def insertionSort1(n, arr):
    num = arr[-1] 
    
    for i in range(n-2, -1, -1): 
        if arr[i] > num:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i+1] = num    
            print(*arr)
            return           
    
    arr[0] = num
    print(*arr)