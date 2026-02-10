class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        double maxDiagSq = 0;
        int maxArea = 0;

        for (int[] dim : dimensions) {
            int l = dim[0];
            int w = dim[1];
            int area = l * w;
            int diagSq = l * l + w * w;

            if (diagSq > maxDiagSq ||
                (diagSq == maxDiagSq && area > maxArea)) {
                maxDiagSq = diagSq;
                maxArea = area;
            }
        }

        return maxArea;
    }
}