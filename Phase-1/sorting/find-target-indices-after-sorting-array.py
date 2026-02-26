class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(1, len(nums)):
            j = i
            while j>0 and nums[j] < nums[j-1]:
                nums[j] , nums[j-1] = nums[j-1], nums[j]
                j-=1
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        return ans

        