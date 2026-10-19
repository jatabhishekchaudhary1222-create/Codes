class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int sum=0;
        int c=0;
        for(int i=0;i<k;i++){
            sum+=arr[i];
        }
        //For the first Window
        if(sum>=k*threshold){
            c++;
        }
        for(int j=k;j<arr.length;j++){
            sum=sum+arr[j]-arr[j-k];
            if(sum>=k*threshold){
                c++;
            }
        }
        return c;
    }
}