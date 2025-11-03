class Solution(object):
    def check(self,nums,mid,k):
        cur_sum=0
        count=0
        for i in nums:
            if cur_sum+i<=mid:
                cur_sum+=i
            else:
                count+=1
                cur_sum=i
        count+=1
        print(count)
        if count==k:
            return True,1
        if count<k:
            return False,1
        return False,0
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low=max(nums)
        high=sum(nums)
        ans=low
        while low<=high:
            mid=(low+high)//2
            print(low,high,mid)
            flag,val=self.check(nums,mid,k)
            if flag:
                ans=mid
                high=mid-1
            else:
                if val==1:
                    high=mid-1
                else:
                    low=mid+1
        return ans

        
