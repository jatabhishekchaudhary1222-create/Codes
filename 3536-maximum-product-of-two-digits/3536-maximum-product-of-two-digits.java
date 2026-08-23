class Solution {
    public int maxProduct(int n) {
        int p=1;
        int max1=0;
        int max2=0;
        while(n>0){
            int ld=n%10;
            n/=10;
            if(ld>max1){
                max2=max1;
                max1=ld;
            }
            else if(ld>max2){
                max2=ld;
            }
        }
        return max1*max2;

    }
}