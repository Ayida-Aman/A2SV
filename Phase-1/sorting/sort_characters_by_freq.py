from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        chars = sorted(list(s))
        count_char = Counter(chars)

        sorted_char = sorted(count_char.items(), key=lambda item: -item[1])
        result = []
        for char, count in sorted_char:
            result.append(char*count)
        return "".join(result)
        """
        :type s: str
        :rtype: str
        """
        