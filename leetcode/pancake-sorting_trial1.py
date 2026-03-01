class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end_idx = len(arr)
        res = []
        while end_idx > 1:
            maxInd = arr.index(end_idx)
            if maxInd == end_idx -1 :
                end_idx-=1
                continue

            if maxInd != 0:
                arr[:maxInd+1] = reversed(arr[:maxInd+1])
                res.append(maxInd+1)
            arr[:end_idx] = reversed(arr[:end_idx])
            res.append(end_idx)

            end_idx-=1
        return res
