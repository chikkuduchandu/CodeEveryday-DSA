class Solution {
    public int numSubarrayWithLessEqualOddnum(int[] nums,int goal){
        int p1=0;
        int p2=0;
        int count=0;
        int ans=0;
        while(p1<nums.length){
            if(nums[p1]%2==1){
                count=count+1;
                if(count<=goal){
                    ans=ans+(p1-p2+1);
                }
                else{
                    while(nums[p2]%2==0){
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
    public int numberOfSubarrays(int[] nums, int k) {
        return numSubarrayWithLessEqualOddnum(nums,k)-numSubarrayWithLessEqualOddnum(nums,k-1);
    }
}
