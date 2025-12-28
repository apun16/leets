class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = {}
        for word in dictionary:
            node = trie
            for c in word: node = node.setdefault(c, {})
            node['#'] = 1
        
        def find(word):
            node, i = trie, 0
            while i < len(word):
                node = node.get(word[i], {})
                if not node: return word
                i += 1
                if '#' in node: return word[:i]
            return word
        
        return ' '.join(find(word) for word in sentence.split())
        