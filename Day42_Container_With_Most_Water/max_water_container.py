class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1=0
        p2=len(height)-1
        ans=0
        while  p1<p2:
            print(ans)
            current_water=(min(height[p1],height[p2])*(p2-p1))
            ans=max(ans,current_water)
            if height[p1]<=height[p2]:
                p1+=1
            else:
                p2-=1
        return ans
        
