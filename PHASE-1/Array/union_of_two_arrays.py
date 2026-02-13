class Solution:    
    def findUnion(self, a, b):
        # code here
        merged = a + b
        my_set = set(merged)
        return list(my_set)