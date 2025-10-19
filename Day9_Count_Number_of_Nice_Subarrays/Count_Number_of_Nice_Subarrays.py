class Solution(object):
    def numberOfSubarraysWithLessOdd(self,nums,goal):
        p1=0
        p2=0
        count=0
        ans=0
        while p1<len(nums):
            #print(p1)
            if nums[p1]%2==1:
                #print(p1)
                count+=1
                if count<=goal:
                    ans+=(p1-p2+1)
                else:
                    while nums[p2]%2==0:
                        p2+=1
                    p2+=1
                    ans+=(p1-p2+1)
                    count-=1
            else:
                if count<=goal:
                    ans+=(p1-p2+1)
            #print(ans,'an')
            p1+=1
        return ans
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        print(self.numberOfSubarraysWithLessOdd(nums,k),self.numberOfSubarraysWithLessOdd(nums,k-1))
        return self.numberOfSubarraysWithLessOdd(nums,k)-self.numberOfSubarraysWithLessOdd(nums,k-1)
        

                        


        
