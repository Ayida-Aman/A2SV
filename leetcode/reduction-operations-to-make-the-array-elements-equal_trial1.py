class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort( )
        op = 0
        minimal_op = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                minimal_op+=1
            op +=minimal_op
        return op