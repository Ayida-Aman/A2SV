class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        r = 0
        k = len(p)
        freq_s = Counter()
        res=[]
        freq_p = Counter(p)
        for r, ch in enumerate(s):
            freq_s[ch] +=1

            if r >=k:
                left = s[r-k]
                freq_s[left] -=1
                if freq_s[left] == 0:
                    del freq_s[left]
            if freq_s == freq_p:
                res.append(r-k+1)
        return res