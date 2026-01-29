class Solution {
    private static final int MOD = 1000000007;

    private long modPow(long base, long exp) {
        long res = 1 % MOD;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1L) == 1L) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }

    public int numberOfWays(String s, String t, long k) {
        int n = s.length();
        if (t.length() != n) return 0;
        if (k == 0) return s.equals(t) ? 1 : 0;

        char[] sc = s.toCharArray();
        char[] tc = t.toCharArray();

        int[] pi = new int[n];
        for (int i = 1, j = 0; i < n; i++) {
            while (j > 0 && tc[i] != tc[j]) j = pi[j - 1];
            if (tc[i] == tc[j]) j++;
            pi[i] = j;
        }
        int totalLen = 2 * n - 1;
        int c0 = 0, c1 = 0;
        for (int i = 0, j = 0; i < totalLen; i++) {
            char c = sc[i < n ? i : i - n];
            while (j > 0 && c != tc[j]) j = pi[j - 1];
            if (c == tc[j]) j++;
            if (j == n) {
                int start = i - n + 1;
                if (start == 0) c0++;
                else c1++;
                j = pi[j - 1];
            }
        }

        if (c0 == 0 && c1 == 0) return 0;
        long invN = modPow(n, MOD - 2);
        long powNm1 = modPow(n - 1, k);
        long sign = ((k & 1L) == 0) ? MOD - 1 : 1; 

        long f1 = (powNm1 + sign) % MOD;
        f1 = (f1 * invN) % MOD;
        long f0 = (f1 + (MOD - sign)) % MOD;

        long ans = ((f0 * c0) % MOD + (f1 * c1) % MOD) % MOD;
        return (int) ans;
    }
}