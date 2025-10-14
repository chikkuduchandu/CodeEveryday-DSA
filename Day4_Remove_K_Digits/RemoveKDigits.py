class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for i in range(len(num)):
            while stack and stack[-1]>int(num[i]) and k>0: 
                stack.pop()
                k-=1
            if num[i]=='0' and not stack:
                continue
            stack.append(int(num[i]))
        ans=''
        while k>0 and stack:
            stack.pop()
            k-=1
        while stack:
            ans+=(str(stack.pop()))
        if ans:
            return ans[-1::-1]
        return '0'
            



        
