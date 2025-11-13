class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        a = 1
        if len(word1) == len(word2):
            for let in word1:
                lst.append(let)
            for let in word2:
                lst.insert(a, let)
                a += 2

        if len(word2) > len(word1):
            counter = 0
            while counter < len(word1):
                for let in word1:
                    lst.append(let)
                    counter += 1
                for let in word2:
                    lst.insert(a, let)
                    a += 2
            else:
                for let in word2[a::1]:
                    lst.insert(a, let)

        if len(word1) > len(word2):
            counter = 0
            while counter < len(word2):
                for let in word1:
                    lst.append(let)
                    counter += 1
                for let in word2:
                    lst.insert(a, let)
                    a += 2
            else:
                for let in word2[a::1]:
                    lst.insert(a, let)

        print(str("".join(lst)))

Solution.mergeAlternately(123,"abc", "pqr")
Solution.mergeAlternately(123,"ab", "pqrs")
Solution.mergeAlternately(123,"abcd", "pq")