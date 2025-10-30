class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans=0
        for i in range(len(s)):
            freq_d={}
            for j in range(i,len(s)):
                if s[j] in freq_d:
                    freq_d[s[j]]+=1
                else:
                    freq_d[s[j]]=1
                ans+=(max(freq_d.values())-min(freq_d.values()))    
        return ans
        
