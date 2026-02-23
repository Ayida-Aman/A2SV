class Solution(object):
    def imageSmoother(self, img):
        n = len(img)
        m = len(img[0])
        new_img = [[0] * m for _ in range (n)]
        
        for i in range(n):
            for j in range(m):
                total = 0
                count = 0
                for x in (i-1, i, i +1):
                    for y in (j-1, j , j+1):
                        if x >= 0 and x<n and y >=0 and y < m:
                            total +=img[x][y]
                            count +=1
                new_img[i][j] = total // count

        return new_img