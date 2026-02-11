class Solution {
    public String shortestPalindrome(String s) {
        int n = s.length();
        String rev = new StringBuilder(s).reverse().toString();
        String combine = s + "#" + rev;
        int[] lps = new int[combine.length()];
        int j = 0;
        
        for (int i = 1; i < combine.length(); i++) {
            while (j > 0 && combine.charAt(i) != combine.charAt(j)) {
                j = lps[j - 1];
            }
            if (combine.charAt(i) == combine.charAt(j)) {
                j++;
            }
            lps[i] = j;
        }
        int k = lps[lps.length - 1];
        return rev.substring(0, n - k) + s;
    }
}
