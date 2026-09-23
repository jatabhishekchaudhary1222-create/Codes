class Solution {
    public int minOperations(int[] nums, int x) {
        int totalsum=0;
        int left=0;
        int maxlen=-1;
        for(int s:nums){
            totalsum+=s;
        }
        int target=totalsum-x;
        if(target<0){
            return -1;
        }
        int sum=0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];

            while(left<=i &&sum>target ){
                sum-=nums[left];
                left++;

            }
            if(target==sum){
                maxlen = Math.max(maxlen, i - left + 1);
            }
        }
        if(maxlen==-1){
            return -1;
        }
        return nums.length-maxlen;
    }
}