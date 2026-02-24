class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}
        for i in range(len(heights)):
            map[heights[i]] = names[i]

        for i in range(len(heights)):
            for j in range(len(heights) - 1):
                if heights[j] < heights[j+1]:
                    heights[j] , heights[j+1] = heights[j+1], heights[j]
        
        ans = []

        for i in range(len(heights)):
            ans.append(map[heights[i]])
        return ans