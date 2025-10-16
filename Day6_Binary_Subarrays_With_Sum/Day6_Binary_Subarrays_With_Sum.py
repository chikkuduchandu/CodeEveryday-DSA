class Solution(object):

    def numSubarrayWithLessOrEqualSum(self,nums,goal):
        p1=0
        p2=0
        count=0
        ans=0
        while p1<len(nums):
            if nums[p1]==1:
                #print(p1)
                count+=1
                if count<=goal:
                    ans+=(p1-p2+1)
                else:
                    while nums[p2]==0:
                        p2+=1
                    p2+=1
                    ans+=(p1-p2+1)
                    count-=1
            else:
                if count<=goal:
                    ans+=(p1-p2+1)
            p1+=1
        return ans


    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        return self.numSubarrayWithLessOrEqualSum(nums,goal)-self.numSubarrayWithLessOrEqualSum(nums,goal-1)

        


                

        





        
