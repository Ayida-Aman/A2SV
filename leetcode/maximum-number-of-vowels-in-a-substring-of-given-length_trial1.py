class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        # r = l = 0
        # max_len = 0

        # while r < len(s):
        #     if s[r] in vowels:
        #         r+=1
        #     else:
        #         max_len = max(max_len, r-l)
        #         r+=1
        #         l = r
        # return max_len

        # l = 0
        # r = k-1
        # count = 0
        # max_count = 0
        # while r<len(s):
        #     m = l
        #     for m in range(r+1):
        #         if s[m] in vowels:
        #             count+=1
        #         else:
        #             break
        #     max_count= max(max_count, count)
        #     l+=1
        #     r+=1
        # return max_count
        count = max_count = 0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        max_count = count

        for r in range(k, len(s)):
            if s[r] in vowels:
                count+=1
            if s[r-k] in vowels:
                count-=1
            max_count=max(max_count, count)
        return max_count