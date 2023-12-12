class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        result = [[0] * rows for _ in range(cols)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][i] = matrix[i][j]
        return result