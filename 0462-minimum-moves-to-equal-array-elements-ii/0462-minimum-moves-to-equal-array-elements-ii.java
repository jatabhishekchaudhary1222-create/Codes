class Solution {
    public int minMoves2(int[] nums) {
        long moves=0;
        int n=nums.length;
        Arrays.sort(nums);
        int med=nums[n/2];
        for(int i=0;i<n;i++){
            moves+=Math.abs((long)nums[i]-med);
        }
        return (int) moves;
    }
}