class Solution:
    def reverseVowels(self, s: str) -> str:
        list_of_vowels = ['a', 'e', 'u', 'o', 'i']
        lst = list(s)
        rev=0
        reversed_lst = []
        for i in range(len(lst), 0, -1):
            if lst[i-1].lower() in list_of_vowels:
                reversed_lst.append(lst[i-1])
        for i in range(len(lst)):
            if lst[i].lower() in list_of_vowels:
                lst[i] = reversed_lst[rev]
                rev += 1
        return "".join(lst)


s = Solution()
print(s.reverseVowels("LEetCode"))
