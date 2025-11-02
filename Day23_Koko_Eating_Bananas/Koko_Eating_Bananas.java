
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int mini=1;
        int maxi=0;
        for(int i=0;i<piles.length;i++){
            if(piles[i]>maxi){
                maxi=piles[i];
            }
        }
        int ans=maxi;
        while(mini<=maxi){

            int mid=(mini+(maxi-mini)/2);
            double count=0;
            for(int i=0;i<piles.length;i++){
                count+=((piles[i]+mid-1)/mid);
                
            }
            if(count<=h){
                maxi=mid-1;
                ans=mid;
                System.out.println(mid+" "+count+" "+h);
            }
            else{
                mini=mid+1;
            }

        }
        return ans;

    }
}
