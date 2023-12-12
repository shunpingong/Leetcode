class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n // 7
        remaining_days = n % 7
        total = weeks * 28
        total += (weeks*(weeks-1)*7)/2
        total += (remaining_days*(remaining_days+1))/2 + weeks * remaining_days
        return total

