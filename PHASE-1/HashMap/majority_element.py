from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        threeshold = len(nums)/2
        freq = Counter(nums)
        for num in nums:
            if freq[num] > threeshold:
                return num
        """
        :type nums: List[int]
        :rtype: int
        """
        