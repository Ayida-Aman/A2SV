class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}
        for i in range(len(heights)):
            map[heights[i]] = names[i]

        for i in range(len(heights) - 1):
            max_idx = i
            for j in range(i+1, len(heights)):
                if heights[j] > heights[max_idx]:
                    max_idx = j
            heights[i], heights[max_idx] = heights[max_idx], heights[i]
        
        ans = []

        for i in range(len(heights)):
            ans.append(map[heights[i]])
        return ans