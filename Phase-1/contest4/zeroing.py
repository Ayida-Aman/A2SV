n = int(input)
arr = list(map(int, input().split))

non_zero = [x for x in arr if x != 0]

if non_zero:
    print(min(non_zero))
    
else:
    print(0)