class Solution {
    public int climbStairs(int n) {
        int a = 1;
        int b = 2;
        int c = 3;

        if (n < 0) return -1;
        if (n == 0) return 1;
        if (n == 1 || n == 2) return n;

        for (int i = 3; i < n+1; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}