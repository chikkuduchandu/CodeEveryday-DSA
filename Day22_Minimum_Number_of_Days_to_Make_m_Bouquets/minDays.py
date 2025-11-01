class Solution(object):
    def check(self,mid,bloomDay,m,k):
        count=0
        boq=0
        for i in bloomDay:
            if i<=mid:
                count+=1
                if count==k:
                    boq+=1
                    count=0
            else:
                count=0
        if boq>=m:
            return True
        return False

    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        mini=min(bloomDay)
        maxi=max(bloomDay)
        ans=-1
        while mini<=maxi:
            mid=(mini+maxi)//2
            print('mid',mid)
            if(self.check(mid,bloomDay,m,k)):
                ans=mid
                maxi=mid-1
            else:
                mini=mid+1
        return ans
