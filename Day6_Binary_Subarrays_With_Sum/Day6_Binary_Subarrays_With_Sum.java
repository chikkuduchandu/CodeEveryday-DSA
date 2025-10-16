class Solution {
    public int numSubarrayWithLessOrEqualSum(int[] nums,int goal){
        int p1=0;
        int p2=0;
        int count=0;
        int ans=0;
        while(p1<nums.length){
            if(nums[p1]==1){
                count=count+1;
                if(count<=goal){
                    ans=ans+(p1-p2+1);
                }
                else{
                    while(nums[p2]==0){
                        p2=p2+1;
                    }
                    p2=p2+1;
                    ans=ans+(p1-p2+1);
                    count=count-1;
                }

            }
            else{
                if(count<=goal){
                    ans=ans+(p1-p2+1);
                }
            }
            p1=p1+1;

        }
        return ans;

    }
    public int numSubarraysWithSum(int[] nums, int goal) {

        return numSubarrayWithLessOrEqualSum(nums,goal)-numSubarrayWithLessOrEqualSum(nums,goal-1);
        
    }
}
