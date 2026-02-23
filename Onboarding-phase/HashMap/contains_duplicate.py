from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        freq = Counter(nums)
        for num in nums:
            if freq[num]>1:
                return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        