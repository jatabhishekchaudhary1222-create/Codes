class Solution {
    public int missingMultiple(int[] nums, int k) {
        int a=1;
        while(true){
            boolean f=false;
            for(int i:nums){
                if(i==k*a){
                    f=true;
                    break;
                }
            }
            if(!f){
                return k*a;
            }
            a++;
        }
    }
}