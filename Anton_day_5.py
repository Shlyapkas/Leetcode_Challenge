class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

        letter_to_turn = [letter for letter in s if letter in vowels]

        letter_to_turn.reverse()

        result_lst = []
        for letter in s:
            if letter in vowels:
                letter = letter_to_turn[0]
                letter_to_turn.pop(0)
                result_lst.append(letter)
            else:
                result_lst.append(letter)

        return "".join(result_lst)


s = "IceCreAm"
# Output: "AceCreIm"
# s = "leetcode"
# Output: "leotcede"


sol = Solution()
print(sol.reverseVowels(s))