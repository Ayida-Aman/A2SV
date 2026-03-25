class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cur_sum = 0
        total = 0
        l = 0
        freq = defaultdict(int)
        for r in range(len(nums)):
            freq[nums[r]] += 1
            cur_sum += nums[r]

            while freq[nums[r]] > 1:
                freq[nums[l]] -= 1
                cur_sum -= nums[l]
                l += 1
            total = max(total, cur_sum)
        return total
