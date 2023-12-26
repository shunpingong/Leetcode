class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero = 0
        ones = s.count('1')
        res = 0

        for i in s[:-1]:
            if i == '0':
                zero +=1
            else:
                ones -= 1
            res = max(res, zero+ones)
        return res