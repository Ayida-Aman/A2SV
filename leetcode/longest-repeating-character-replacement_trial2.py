class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count = l = 0
        # c = Counter(s)
        # char = max(c, key=c.get)
        # # print (char)
        # freq = {}
        # for i in range(len(s)):
            
        #     if s[i] != char and k==0:
        #         if s[l] != char:
        #             k+=1
        #         l +=1
        #     elif s[i] != char and k>0:
        #         k-=1
        #     count = max(i-l+1, count)
        # return count

        count = l = 0
        c = Counter(s)
        freq = Counter()
        for i in range(len(s)):
            freq[s[i]] +=1
            max_freq = max(freq.values())
            cur_len = i - l +1
            if cur_len - max_freq > k:
                freq[s[l]] -=1
                l+=1
            count = max(count,i-l+1)
        return count

