class Solution(object):
    def minimumRecolors(self, blocks, k):
        flip = 0
        l = 0
        res = float('inf')
        for r in range(len(blocks)):
            if blocks[r] != "B":
                flip +=1
            if r-l+1 == k:
                res = min(res, flip)
                if blocks[l] != "B":
                    flip -=1
                l+=1
        return res
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        