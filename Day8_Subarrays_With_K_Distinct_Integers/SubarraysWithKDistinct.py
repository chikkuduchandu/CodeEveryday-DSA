class Solution(object):
    def numberOfStringsLessOrEqualThreeChar(self,nums,k):
        d=dict()
        p1=0
        p2=0
        ans=0
        while p1<len(nums):
            if nums[p1] in d:
                d[nums[p1]]+=1
            else:
                d[nums[p1]]=1
            if len(d)<=k:
                ans+=(p1-p2+1)
            else:
                while len(d)>k:
                    d[nums[p2]]-=1
                    if d[nums[p2]]==0:
                        del d[nums[p2]]
                    p2+=1
                ans+=(p1-p2+1)
            p1+=1
        return ans

    
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.numberOfStringsLessOrEqualThreeChar(nums,k)-self.numberOfStringsLessOrEqualThreeChar(nums,k-1)
        
