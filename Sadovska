class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = []
        n = min(len(word1), len(word2))

        if len(word1) == len(word2):
            for i in range(n):
                result.append(word1[i])
                result.append(word2[i])

        elif len(word1) > len(word2):
            for i in range(n):
                result.append(word1[i])
                result.append(word2[i])
            for i in range(len(word1)):
                if i >= n:
                    result.append(word1[i])
        elif len(word2) > len(word1):
            for i in range(n):
                result.append(word1[i])
                result.append(word2[i])
            for i in range(len(word2)):
                if i >= n:
                    result.append(word2[i])
        return "".join(result)

s = Solution()
print(s.mergeAlternately('abs', 'rewh'))
