class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> ans=new ArrayList<>();
        int max=candies[0];
        for(int i=1;i<candies.length;i++){
            if(candies[i]>max){
                max=candies[i];
            }
        }
            for(int j=0;j<candies.length;j++){
                if(candies[j]+extraCandies>=max){
                    ans.add(true);
                }
                else{
                    ans.add(false);
                }
            }
        return ans;
    }
}