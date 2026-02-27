def countingSort(arr):
    new_arr = [0] * 100
    
    for i in range(len(arr)):
        new_arr[arr[i]]+=1
    return new_arr