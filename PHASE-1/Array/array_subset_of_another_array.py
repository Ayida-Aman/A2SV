#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a_freq = Counter(a)
        b_freq = Counter(b)
        boolean = True
        for num in b:
            if a_freq[num] < b_freq[num]:
                boolean = False
        return boolean
        
    
    
    
    
