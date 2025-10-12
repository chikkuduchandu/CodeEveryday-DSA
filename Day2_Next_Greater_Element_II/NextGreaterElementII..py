class Solution:
    def ceil(self,key,arr):
        if arr:
            ans=-1
            low=0
            high=len(arr)-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>key:
                    high=mid-1
                    ans=arr[mid]
                elif arr[mid]<=key:
                    low=mid+1
            return ans
        else:
            return -1
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        ans=[-1 for i in range(len(nums))]
        flag=[0 for i in range(len(nums))]
        for i in range(len(nums)-1,-1,-1):
            if stack:
                while stack and stack[-1]<=nums[i]:
                    stack.pop()
                if stack:
                    ans[i]=stack[-1]
                    flag[i]=1
            stack.append(nums[i])
        #print(ans)
        my_arr=[]
        for i in range(len(nums)):
            # print(my_arr)
            # print(ans)
            if flag[i]==0:
                ans[i]=self.ceil(nums[i],my_arr)
                flag[i]=1
            if my_arr:
                if my_arr[-1]<nums[i]:
                    my_arr.append(nums[i])
            else:
                my_arr.append(nums[i])
        return ans

                


        
