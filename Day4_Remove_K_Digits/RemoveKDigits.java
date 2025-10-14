class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Integer> stack=new Stack<>();
        for(int i=0;i<num.length();i++){
            while( !stack.isEmpty() && stack.peek()>
            (num.charAt(i)-'0') && k>0){
                stack.pop();
                k=k-1;
            }
            if( num.charAt(i)=='0' && stack.isEmpty()){
                continue;
            }
            stack.push(num.charAt(i)-'0');
            //System.out.println('B'-'A');
        }
        String ans="";
        while(k>0 && !stack.isEmpty()){
            stack.pop();
            k=k-1;
        }
        while(!stack.isEmpty()){
            ans=ans+(stack.pop());

        }
        
        if(ans.length()!=0){
            StringBuilder sb=new StringBuilder(ans);
            return sb.reverse().toString();
        }
        return "0";
    }
}
