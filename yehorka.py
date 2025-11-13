class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result_lst = []
        if len(word1) == len(word2):
            for i in range(0, len(word1)):
                result_lst.append(word1[i])
                result_lst.append(word2[i])
        elif len(word1) > len(word2):
            for i in range(0, len(word2)):
                result_lst.append(word1[i])
                result_lst.append(word2[i])
            for i in range(len(word2), len(word1)):
                result_lst.append(word1[i])
        else:
            for i in range(0, len(word1)):
                result_lst.append(word1[i])
                result_lst.append(word2[i])
            for i in range(len(word1), len(word2)):
                result_lst.append(word2[i])
        result = "".join(result_lst)
        return result
s = Solution()
print(s.mergeAlternately("bebra", "popa"))
