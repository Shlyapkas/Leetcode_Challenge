class Solution:
    def reverseWords(self, s: str) -> str:
        split_lst = s.split(" ")

        # видаляємо всі пробіли
        normal_lst = [x for x in split_lst if x != ""]
        
        normal_lst.reverse()
        result = " ".join(normal_lst)

        return result


s = "the sky is blue"
# s = "    hello   world"
# s = "a good   example"
sol = Solution()
print(sol.reverseWords(s))
