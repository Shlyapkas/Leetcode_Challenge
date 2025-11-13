class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        n = 1
        for i in word2:
            word1.insert(n, i)
            n += 2
        return "".join(word1)