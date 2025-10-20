class Solution(object):
    def findCombinations(self,candidates,ind,target,curr_sum,ans,curr_list):
        if curr_sum==target:
            ans.append(curr_list)
            return
        if curr_sum>target or ind==len(candidates):
            return
         
        self.findCombinations(candidates,ind,target,curr_sum+candidates[ind],ans,curr_list+[candidates[ind]])
        self.findCombinations(candidates,ind+1,target,curr_sum,ans,curr_list)
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ans=[]
        self.findCombinations(candidates,0,target,0,ans,[])
        return ans
        
