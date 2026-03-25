class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        window_len = len(s1)

        for i in range(len(s2) - window_len + 1):
            substring = s2[i:i+window_len]
            counter_sub = Counter(substring)

            if counter_sub == counter_s1:
                return True
        return False