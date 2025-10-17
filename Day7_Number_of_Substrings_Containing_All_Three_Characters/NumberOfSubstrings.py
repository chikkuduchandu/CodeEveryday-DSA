
class Solution(object):
    def numberOfStringsLessOrEqualThreeChar(self,s,k):
        d=dict()
        p1=0
        p2=0
        ans=0
        while p1<len(s):
            if s[p1] in d:
                d[s[p1]]+=1
            else:
                d[s[p1]]=1
            if len(d)<=k:
                ans+=(p1-p2+1)
            else:
                while len(d)>k:
                    d[s[p2]]-=1
                    if d[s[p2]]==0:
                        del d[s[p2]]
                    p2+=1
                ans+=(p1-p2+1)
            p1+=1
        return ans
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.numberOfStringsLessOrEqualThreeChar(s,3)-self.numberOfStringsLessOrEqualThreeChar(s,2)

        






        
