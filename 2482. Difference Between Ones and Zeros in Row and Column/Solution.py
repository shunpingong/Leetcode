class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])

        row_ones = [0] * m
        col_ones = [0] * n 
        diff = [[0] * n for _ in range(m)]

        # Count ones in each row and column
        for r in range(m):
            for c in range(n):
                if (grid[r][c]==1):
                    row_ones[r] +=1
                    col_ones[c] +=1
                else:
                    row_ones[r] -=1
                    col_ones[c] -=1

        # Calculate the difference matrix
        for r in range(m):
            for c in range(n):
                diff[r][c] = row_ones[r] + col_ones[c]

        return diff