class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i in s if i in "aoeuiAOEUI"]
        for i in ("a", "o", "e", "u", "i", "A", "O", "E", "U", "I"):
            s = s.replace(i, "і")
        for i in vowels[::-1]:
            s = s.replace("і", i, 1)
        return s
