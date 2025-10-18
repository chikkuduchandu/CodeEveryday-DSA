class Solution {
    public int subarraysWithLessOrKDistinct(int[] nums,int k){
        int p1=0;
        int p2=0;
        HashMap<Integer,Integer> m=new HashMap<>();
        int ans=0;
        while(p1<nums.length){

            if(m.containsKey(nums[p1])){
                m.put(nums[p1],m.get(nums[p1])+1);
            }
            else{
                m.put(nums[p1],1);
            }
            if( m.size()<=k){
                ans+=(p1-p2+1);
            }
            else{
                while(m.size()>k){
                    m.put(nums[p2],m.get(nums[p2])-1);
                    if (m.get(nums[p2])==0){
                        m.remove(nums[p2]);
                    }
                    p2+=1;
                }
                ans+=(p1-p2+1);
            }
            p1+=1;

        }
        return ans;
    }
    public int subarraysWithKDistinct(int[] nums, int k) {
        return subarraysWithLessOrKDistinct(nums,k)-subarraysWithLessOrKDistinct(nums,k-1);
        
    }
}
