class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        res = []
        i = 0
        j = n-1

        while i<=j:
            if arr[i] == 0:
                res.extend([0] * 2)
                j -=1
            else:
                res.append(arr[i])
            
            i+=1
        arr[:] = res[:n]
        """
        Do not return anything, modify arr in-place instead.
        """
        