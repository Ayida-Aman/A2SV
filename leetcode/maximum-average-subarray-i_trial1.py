class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float('-inf')

        for i in range(len(nums)):
            total = 0
            count = 0

            for j in range(i, i+k):
                if j < len(nums):
                    total += nums[j]
                    count+=1
            if count == k:
                avg = total / k
                maxAvg = max(avg, maxAvg)
        return maxAvg