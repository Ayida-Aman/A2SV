class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        m = total
        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i - k]
            m = max(m , total)
        return m / k