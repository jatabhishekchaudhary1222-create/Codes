class Solution {
    public int maxProfit(int[] prices) {

        int max_p = 0;
        int mi = prices[0];

        for (int i = 1; i < prices.length; i++) {

            if (prices[i] < mi) {
                mi = prices[i];
            }

            int profit = prices[i] - mi;

            if (profit > max_p) {
                max_p = profit;
            }
        }

        return max_p;
    }
}