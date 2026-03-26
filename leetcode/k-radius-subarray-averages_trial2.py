class Solution(object):
    def getAverages(self, nums, k):
        res = [-1] * len(nums)
        l = 0
        size = 2 * k +1
        total = sum(nums[l:size])
        if size > len(nums):
            return res
        res[k] = total // size
        for i in range(k+1, len(nums)-k):
            total-=nums[l]
            total+=nums[i+k]
            res[i] = total // size
            l+=1
        return res


        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        