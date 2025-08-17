class Solution {
    public int solution(int n, int k) {
        int s = n/10;
        k -= s;
        return (12000*n) + (2000*k);
    }
}