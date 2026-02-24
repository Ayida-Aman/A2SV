class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}
        for i in range(len(heights)):
            map[heights[i]] = names[i]

        for i in range(1 , len(heights) ):
            j = i-1
            while j>=0:
                if heights[j+1] > heights[j]:
                    heights[j+1] , heights[j] = heights[j] , heights[j+1]
                j-=1      
        ans = []

        for i in range(len(heights)):
            ans.append(map[heights[i]])
        return ans