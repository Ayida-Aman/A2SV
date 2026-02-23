class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for row in image:
            r = []
            for i in reversed(row):
                r.append(i^1)
            res.append(r)
        return res