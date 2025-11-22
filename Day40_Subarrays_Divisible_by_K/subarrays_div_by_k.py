class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix=[0 for i in range(len(nums))]
        d=dict()
        d[0]=1
        count=0
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        for i in range(len(nums)):
            if prefix[i]%k in d:
                count+=d[prefix[i]%k]
                d[prefix[i]%k]+=1
            else:
                d[prefix[i]%k]=1
        return count

        print(prefix)
        
