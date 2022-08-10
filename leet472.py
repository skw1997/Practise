class Solution():
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        trie, ans = Trie(), []
        for word in sorted(words, key=len):
            if word == "":
                continue
            if trie.find(word):
                ans.append(word)
            else:
                trie.insert(word)
        return ans

    class Trie:
        def __init__(self):
            self.root = {}

        def insert(self, word):
            node = self.root
            for w in word + "#":
                if w not in node:
                    node[w] = {}
                node = node[w]

        def find(self, word):
            node = self.root
            for i in range(len(word)):
                if "#" in node:
                    if self.find(word[i:]):
                        return True
                if word[i] in node:
                    node = node[word[i]]
                else:
                    return False
            return "#" in node



