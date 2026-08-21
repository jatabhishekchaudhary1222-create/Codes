class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] out=new int[2*n];
        int pre=0;
        for(int i=0;i<n;i++){
            out[pre]=nums[i];
            pre++;
            out[pre]=nums[i+n];
            pre++;
        }
        return out;
    }
}