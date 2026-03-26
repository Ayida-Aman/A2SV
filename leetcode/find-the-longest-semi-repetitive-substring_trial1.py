class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        n = len(s)
        if n == 1:
            return 1
        end_found = None
        start , end = 0,1
        ans = 1
        while end < n:
            ch = s[end]
            if ch == s[end-1]:
                if end_found == None:
                    end_found = end
                else:
                    start = end_found
                    end_found = end
            ans = max(ans,end-start+1)
            end += 1
        return ans
 

        """
        :type s: str
        :rtype: int
        """
        