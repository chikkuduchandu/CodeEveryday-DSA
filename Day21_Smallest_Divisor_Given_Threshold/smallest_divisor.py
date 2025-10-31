import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        mini=1
        maxi=max(nums)
        ans=maxi
        while mini<=maxi:
            mid=(mini+maxi)//2
            summ=0
            for i in nums:
                summ+=(math.ceil(float(i)/mid))
            if summ<=threshold:
                ans=mid
                maxi=mid-1
            elif summ>threshold:
                mini=mid+1
        return ans
        



        
