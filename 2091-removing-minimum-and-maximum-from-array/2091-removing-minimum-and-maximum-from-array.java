class Solution {
    public int minimumDeletions(int[] nums) {
        int a=0;
        int b=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]<nums[a]){
                a=i;
            }
            if(nums[i]>nums[b]){
                b=i;
            }
        }
         int left=Math.min(a,b);
         int right=Math.max(a,b);
         int front=right+1;
         int back=nums.length-left;
         int both=(left+1)+(nums.length-right);
         return Math.min(front,Math.min(back,both));
    }
}