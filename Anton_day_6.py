
# Example 1:
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution:
    def reverseWords(self, s: str) -> str:
        split_lst = s.split(" ")


        normal_lst = [x for x in split_lst if x != ""]
        normal_lst.reverse()
        result = " ".join(normal_lst)

        return result



# s = "the sky is blue"
s = "    hello   world"
# s = "a good   example"
sol = Solution()
print(sol.reverseWords(s))
