class Solution:
    def reverseWords(self, s: str) -> str:
        lst = list(s.split())
        lst_reversed = []
        for i in range(len(lst), 0, -1):
            lst_reversed.append(lst[i-1])
            if i != 1:
                lst_reversed.append(" ")
        print(lst)
        print(lst_reversed)
        return "".join(lst_reversed)


s = Solution()
print(s.reverseWords("  hello world"))
