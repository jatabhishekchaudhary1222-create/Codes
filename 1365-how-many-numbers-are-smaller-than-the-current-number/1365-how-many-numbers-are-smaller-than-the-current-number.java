class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int n=nums.length;
        int []a=new int[n];; 
        for(int i=0;i<n;i++){
            int c=0;
            for(int j=0;j<n;j++){
                if(j!=i){
                    if(nums[j]<nums[i]){
                        c++;
                    }
                }
            }
            a[i]=c;
        }
        return a;
    }
}