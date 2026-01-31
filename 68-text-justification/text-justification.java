class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int index = 0;
        int totals = words.length;
      
        while (index < totals) {
            List<String> current = new ArrayList<>();
            current.add(words[index]);
            int length = words[index].length();
            index++;

            while (index < totals && 
                   length + 1 + words[index].length() <= maxWidth) {
                length += 1 + words[index].length();
                current.add(words[index]);
                index++;
            }
          
            if (index == totals || current.size() == 1) {
                String left = String.join(" ", current);
                String padding = " ".repeat(maxWidth - left.length());
                result.add(left + padding);
                continue;
            }
            int spaces = maxWidth - (length - current.size() + 1);
            int wordSpace = spaces / (current.size() - 1);
            int extra = spaces % (current.size() - 1);
          
            StringBuilder currentLine = new StringBuilder();
            for (int i = 0; i < current.size() - 1; i++) {
                currentLine.append(current.get(i));
                int add = wordSpace + (i < extra ? 1 : 0);
                currentLine.append(" ".repeat(add));
            }
            currentLine.append(current.get(current.size() - 1));
          
            result.add(currentLine.toString());
        }
        return result;
    }
}