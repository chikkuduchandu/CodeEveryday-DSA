class Solution {
    public void findCombinations(int[] candidates,int ind,int target,int curr_sum,List<List<Integer>> ans,List<Integer> curr_list){
        if(curr_sum==target){
            ans.add(new ArrayList(curr_list));
            return;
        }
        if(curr_sum>target || ind==candidates.length){
            return;
        }
        curr_list.add(candidates[ind]);
        findCombinations(candidates,ind,target,curr_sum+candidates[ind],ans,curr_list);
        curr_list.remove(curr_list.size()-1);
        findCombinations(candidates,ind+1,target,curr_sum,ans,curr_list);
    }
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> curr_list=new ArrayList<>();
        findCombinations(candidates,0,target,0,ans,curr_list );
        return ans;
    }
}
