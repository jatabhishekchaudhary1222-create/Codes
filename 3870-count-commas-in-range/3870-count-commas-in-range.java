class Solution {
    public int countCommas(int n) {
        int c=0;
        int ans=0;
        for(int i=1;i<=n;i++){
            int d=String.valueOf(i).length();
            if(d>=4){
                ans+=(d-1)/3;
            }
        }
        return ans;
    }
}