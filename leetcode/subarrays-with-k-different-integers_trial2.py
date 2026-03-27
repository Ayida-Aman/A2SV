class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l = m = 0
        res = 0

        for r in range(len(nums)):
            freq[nums[r]] +=1

            while len(freq) > k:
                freq[nums[m]] -=1
                if  freq[nums[m]] == 0:
                    del freq[nums[m]]
                m+=1
                l = m
            while freq[nums[m]] > 1:
                freq[nums[m]] -=1
                m+=1

            if len(freq) == k:
                res+=m-l+1
        return res