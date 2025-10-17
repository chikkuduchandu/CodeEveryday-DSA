class Solution {
    public int numberOfStringsLessOrEqualThreeChar(String s,int k){
        HashMap<Character,Integer> m=new HashMap<>();
        int p1=0;
        int p2=0;
        int ans=0;

        while(p1<s.length()){
            if( m.containsKey(s.charAt(p1))){
                m.put(s.charAt(p1),m.get(s.charAt(p1))+1);
            }
            else{
                m.put(s.charAt(p1),1);
            }
            if(m.size()<=k){
                ans+=(p1-p2+1);
            }
            else{
                while(m.size()>k){
                    m.put(s.charAt(p2),m.get(s.charAt(p2))-1);
                    if (m.get(s.charAt(p2))==0){
                        m.remove(s.charAt(p2));
                    }
                    p2+=1;
                }
                ans+=(p1-p2+1);
            }
            p1+=1;
        }
        return ans;


    }
    public int numberOfSubstrings(String s) {
        return numberOfStringsLessOrEqualThreeChar(s,3)-numberOfStringsLessOrEqualThreeChar(s,2);
        
    }
}
