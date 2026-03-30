class Solution(object):
    def runningSum(self, nums):
        l=[]
        s=0
        for num in nums:
            s+=num
            l.append(s)
        return l
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        