import java.util.HashMap;
class Solution {
    public int largestOverlap(int[][] img1, int[][] img2) {
        HashMap<String,Integer> map=new HashMap<>();
        int max=0;
        for(int i=0;i<img1.length;i++){
            for(int j=0;j<img2.length;j++){
                if(img1[i][j]==1){
                    for(int a=0;a<img2.length;a++){
                        for(int b=0;b<img2.length;b++){
                            if(img2[a][b]==1){
                                int dr=a-i;
                                int dc=b-j;
                                String k=dr+","+dc;
                                int c=map.getOrDefault(k,0)+1;
                                map.put(k,c);
                                max=Math.max(max,c);
                            }
                        }
                    }
                }
            }
        }
        return max;
    }
}