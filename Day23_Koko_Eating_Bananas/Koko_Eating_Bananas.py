import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        mini=1
        maxi=max(piles)
        ans=maxi
        while mini<=maxi:
            mid=(mini+maxi)//2
            count=0
            for i in piles:
                count+=math.ceil(float(i)/mid)
            if count<=h:
                maxi=mid-1
                ans=mid
            else:
                mini=mid+1
        return ans
        
        
        
