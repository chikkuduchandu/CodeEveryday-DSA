class Solution {
    public void findCombinations(int ind,int[] candidates,int target, List<List<Integer>> ans,List<Integer> curr_list){
        if(target==0){
            ans.add(new ArrayList(curr_list));
            return;
        }
        if(ind==candidates.length || candidates[ind]>target){
            return;
        }
        for(int i=ind;i<candidates.length;i++){
            if(i>ind && candidates[i]==candidates[i-1]){
                continue;
            }
            curr_list.add(candidates[i]);
            findCombinations(i+1,candidates,target-candidates[i],ans,curr_list);
            curr_list.remove(curr_list.size()-1);
        }
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {

        Arrays.sort(candidates);
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> curr_list=new ArrayList<>();
        findCombinations(0,candidates,target,ans,curr_list);

        return ans;
    }
}
