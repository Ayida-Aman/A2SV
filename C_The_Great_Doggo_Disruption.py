from collections import Counter


n = int(input())
string = list(input())

# freq = Counter(string)

# singles = sum (1 for s in freq.values() if s >= 2)

# if singles>=1:
#     print("Yes")
# else:
#     print("No")

# if len(set(string)) == n:
#     print("No")
# else:
#     print("Yes")

if list(set(string)) == 1:
    print("Yes")
elif len(string) == len(list (set(string))):
    print("No")
else:
    def Dog_Disruption(string):
        set_string = list (set(string))
        counter = Counter(string)

        j = 0

        for i in range(len(set_string)):
            if counter[set_string[i]] >= 2:
                while j < counter[set_string[i]]:
                    string[j] = set_string[i+1]
                    j+=1
    if len(list (set(string)) ) == 1:
        print("Yes")
    else:
        Dog_Disruption(string)