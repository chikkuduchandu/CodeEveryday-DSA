class Solution {
    public int beautySum(String s) {
        int ans=0;
        for(int i=0;i<s.length();i++){
            HashMap<Character,Integer> m=new HashMap<>();
            for(int j=i;j<s.length();j++){
                if(m.containsKey(s.charAt(j))){
                    m.put(s.charAt(j),m.get(s.charAt(j))+1);
                }
                else{
                    m.put(s.charAt(j),1);
                }
                int mini=Collections.min(m.values());
                int max=Collections.max(m.values());
                ans+=(max-mini);
            }
        }
        return ans;
    }
}
