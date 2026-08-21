class Solution {
    public int maximumWealth(int[][] accounts) {
         int maxw=0;
        for(int i=0;i<accounts.length;i++){
            int s=0;
            for(int j=0;j<accounts[i].length;j++){
                s+=accounts[i][j];
            }
            maxw=Math.max(maxw,s);
        }
        return maxw;
        
    }
}