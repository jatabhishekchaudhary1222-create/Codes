class Solution {
    public String[] createGrid(int m, int n) {
        char[][] grid= new char[m][n];
        //Obstacles
        for(int i=0;i<m;i++){
            Arrays.fill(grid[i],'#');
        }
        //For first row
        for(int j=0;j<n;j++){
            grid[0][j]='.';
        }
        // For last col
        for(int i=0;i<m;i++){
            grid[i][n-1]='.';
        }
        String[] res= new String[m];
        for(int i=0;i<m;i++){
            res[i]=new String(grid[i]);
        }
        return res;
    }
}