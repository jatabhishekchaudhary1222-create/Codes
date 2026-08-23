class Solution {
    public boolean checkDivisibility(int n) {
        int o=n;
        int s=0;
        int p=1;
        while(n!=0){
            int ld=n%10;
            s+=ld;
            p*=ld;
            n/=10;
        }
        return (o%(s+p)==0);

    }
}