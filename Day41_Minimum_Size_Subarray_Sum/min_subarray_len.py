class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        p1=0
        p2=0
        ans=0
        current_sum=0
        while p1<len(nums):
            current_sum+=nums[p1]
            if current_sum>=target:

                while current_sum>=target:
                    if ans==0:
                        ans=p1-p2+1
                    else:
                        ans=min(ans,p1-p2+1)
                    current_sum-=nums[p2]
                    p2+=1
            p1+=1
        if ans:
            return ans
        return 0
        
                
            
        
