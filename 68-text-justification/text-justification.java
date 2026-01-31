class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int currIndex = 0;
        while (currIndex < words.length) {
            int nextIndex = currIndex + 1;
            int lineLength = words[currIndex].length();
            while (nextIndex < words.length && lineLength + 1 + words[nextIndex].length() <= maxWidth) {
                lineLength += words[nextIndex].length() + 1;
                nextIndex++;
            }
            int numWords = nextIndex - currIndex;
            StringBuilder line = new StringBuilder();
            if (nextIndex == words.length || numWords == 1) {
                // Left-justified (last line or single word)
                for (int k = currIndex; k < nextIndex; k++) {
                    line.append(words[k]);
                    if (k < nextIndex - 1) {
                        line.append(" ");
                    }
                }
                while (line.length() < maxWidth) {
                    line.append(" ");
                }
            } else {
                // Fully justified
                int totalSpaces = maxWidth;
                for (int k = currIndex; k < nextIndex; k++) {
                    totalSpaces -= words[k].length();
                }
                int baseSpaces = totalSpaces / (numWords - 1);
                int extraSpaces = totalSpaces % (numWords - 1);
                for (int k = currIndex; k < nextIndex; k++) {
                    line.append(words[k]);
                    if (k < nextIndex - 1) {
                        for (int s = 0; s < baseSpaces; s++) {
                            line.append(" ");
                        }
                        if (extraSpaces > 0) {
                            line.append(" ");
                            extraSpaces--;
                        }
                    }
                }
            }
            result.add(line.toString());
            currIndex = nextIndex;
        }
        return result;
    }
}