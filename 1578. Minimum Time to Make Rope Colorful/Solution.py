class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        l = time = 0
        r = 1
        while r<len(colors):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    time += neededTime[l]
                    l = r
                else:
                    time += neededTime[r]
            else:
                l=r
            r+=1
        return time