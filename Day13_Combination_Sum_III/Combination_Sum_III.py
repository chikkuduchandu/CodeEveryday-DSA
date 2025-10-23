class Solution(object):
    def findCombinations(self,ind,curr_num,k,n,curr_list,curr_sum,ans):
        if curr_sum==n and ind==k:
            
            ans.append(curr_list)
            return
        if k==ind:
            return
        for i in range(curr_num,10):
            self.findCombinations(ind+1,i+1,k,n,curr_list+[i],curr_sum+i,ans)


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        
        self.findCombinations(0,1,k,n,[],0,ans)
        return ans

        
