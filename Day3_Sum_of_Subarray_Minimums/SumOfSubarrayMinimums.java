class Triplet{
    int a,b,c;
    Triplet(int a,int b,int c){
        this.a=a;
        this.b=b;
        this.c=c;
    }
}
class Solution {
    public int sumSubarrayMins(int[] arr) {
        long m=(long)(1e9+7);
        long minis_sum=arr[arr.length-1];
        Stack<Triplet>stack=new Stack<>();
        stack.push(new Triplet(arr[arr.length-1],arr[arr.length-1],arr.length-1));

        for(int i=arr.length-2;i>=0;i--){
            while(!stack.isEmpty() && stack.peek().a>arr[i]){
                stack.pop();
            }
            if(!stack.isEmpty()){
                minis_sum+=((stack.peek().c-i)*arr[i]+stack.peek().b);
                stack.push(new Triplet(arr[i],(stack.peek().c-i)*arr[i]+stack.peek().b,i));
            }
            else{
                minis_sum+=(arr[i]*(arr.length-i));
                stack.push(new Triplet(arr[i],arr[i]*(arr.length-i),i));
            }
        }
        return (int)(minis_sum%m);
        
    }
}
