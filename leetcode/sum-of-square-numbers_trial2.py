class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        num = int(sqrt(c))+1
        arr = []
        for i in range(num):
            arr.append(i)

        l = 0
        r = len(arr)-1
        while l<=r:
            if arr[l] * arr[l] + arr[r] * arr[r] > c:
                r-=1
            elif arr[l] * arr[l] + arr[r] * arr[r] < c:
                l+=1
            elif arr[l] * arr[l] + arr[r] * arr[r] == c:
                return True
        return False