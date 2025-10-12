class Solution {
    public int getCeil(int key,List<Integer> arr){
        if(!arr.isEmpty()){
            int ans=-1;
            int low=0;
            int high=arr.size()-1;

            while(low<=high){
                int mid=low+(high-low)/2;
                if(arr.get(mid)>key){
                    ans=arr.get(mid);
                    high=mid-1;
                }
                else if(arr.get(mid)<=key){
                    low=mid+1;
                }
            }
            return ans;
        }
        return -1;
    }
    public int[] nextGreaterElements(int[] nums) {

        Stack<Integer> s=new Stack<>();

        int ans[]=new int[nums.length];
        for(int i=0;i<ans.length;i++){
            ans[i]=-1;
        }
        int flag[]=new int[nums.length];
        
        for(int i=nums.length-1;i>=0;i--){
            if(!s.isEmpty()){
                while( (!s.isEmpty())&& s.peek()<=nums[i]){
                    s.pop();
                }
                if(!s.isEmpty()){
                    ans[i]=s.peek();
                    flag[i]=1;
                }
            }
            s.push(nums[i]);
        }
        for(int i=0;i<ans.length;i++){
            System.out.print(ans[i]+" ");
        }
        System.out.println();

        List<Integer> my_arr=new ArrayList<>();

        for(int i=0;i<nums.length;i++){
            if(flag[i]==0){
                ans[i]=getCeil(nums[i],my_arr);
            }
            if(my_arr.size()==0){
                my_arr.add(nums[i]);
            }
            else{
                if(my_arr.get(my_arr.size()-1)<nums[i]){
                    my_arr.add(nums[i]);
                }
            }
        }

        return ans;
    }
}
