class Solution(object):
    def balancedString(self, s):
        freq = Counter(s)
        l = 0
        res = float('inf')
        balance = len(s)/4

        if max(freq.values()) == balance:
            return 0
        for r in range(len(s)):
            freq[s[r]] -=1

            while l<=r and max(freq.values()) <= balance:
                res = min(res, r-l+1)
                freq[s[l]] +=1
                l+=1
        return res


        """
        :type s: str
        :rtype: int
        """