class Solution(object):
    def maxTurbulenceSize(self, arr):
        count = 0
        max_count1 = max_count2 = 0
        diff = []
        count1 = count2 = 1
        if len(arr) == 1:
            return 1
        for i in range(len(arr)-1):
            if i%2==0 and arr[i] > arr[i+1] :
                count1 +=1
            elif i%2!=0 and arr[i] < arr[i+1] :
                count1 +=1
            else:
                max_count1 = max(count1, max_count1)
                count1 = 1
        for i in range(len(arr)-1):
            if i%2==0 and arr[i] < arr[i+1] :
                count2 +=1
            elif i%2!=0 and arr[i] > arr[i+1] :
                count2 +=1
            else:
                max_count2 = max(count2, max_count2)
                count2  = 1
        max_count1 = max(count1, max_count1)
        max_count2 = max(count2, max_count2)
        return max(max_count1, max_count2)
            
                
        """
        :type arr: List[int]
        :rtype: int
        """
        