class Solution(object):
    def findCombinations(self,ind,candidates,target,ans,curr_list):
        if target==0:
            ans.append(curr_list)
            return
        if ind==len(candidates) or candidates[ind]>target:
            return
        for i in range(ind,len(candidates)):
            if i>ind and candidates[i]==candidates[i-1]:
                continue
            self.findCombinations(i+1,candidates,target-candidates[i],ans,curr_list+[candidates[i]])
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans=[]
        self.findCombinations(0,candidates,target,ans,[])
        return ans

        
