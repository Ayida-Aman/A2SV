class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        l = 0
        count_pairs = 0
        res = 0
        for r in range(len(nums)):
            count_pairs += count[nums[r]]
            count[nums[r]] += 1

            while count_pairs >= k:
                res += len(nums) - r 
                count[nums[l]] -= 1
                count_pairs -= count[nums[l]]
                l += 1
        return res