class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        M=(10**9+7)
        minis_sum=arr[-1]
        stack=[(arr[-1],arr[-1],len(arr)-1)]

        for i in range(len(arr)-2,-1,-1):
            
            while stack and arr[i]<stack[-1][0]:
                stack.pop()
            if stack:
                #print((stack[-1][2]-i))
                minis_sum+=((stack[-1][2]-i)*(arr[i])+stack[-1][1])
                stack.append((arr[i],(stack[-1][2]-i)*(arr[i])+stack[-1][1],i))
            else:
                minis_sum+=(arr[i]*(len(arr)-i))
                stack.append((arr[i],arr[i]*(len(arr)-i),i))
            #print(i,minis_sum,stack)
        return minis_sum%M


        
        

            
        
