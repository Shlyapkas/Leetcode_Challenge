class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for i in range(s.count("")):
            s.remove("")
        s = " ".join(s[::-1])
        return s
