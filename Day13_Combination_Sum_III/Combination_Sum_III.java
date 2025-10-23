class Solution {
    public void findCombinations(int ind,int curr_num,int k,int n,List<Integer> curr_list,int curr_sum,List<List<Integer>> ans){
        if(curr_sum==n && ind==k){
            ans.add(new ArrayList(curr_list));
            return;
        }
        if(k==ind){
            return;
        }
        for(int i=curr_num;i<10;i++){
            curr_list.add(i);
            findCombinations(ind+1,i+1,k,n,curr_list,curr_sum+i,ans);
            curr_list.remove(curr_list.size()-1);
        }
        
    } 
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> curr_list=new ArrayList<>();
        findCombinations(0,1,k,n,curr_list,0,ans);
        return ans;
    }
}
