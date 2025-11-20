class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        mult = 1
        for i in nums:
            if i != 0:
                mult *= i
        try:
            answer = list(map(lambda x: int(mult / x), nums))
        except ZeroDivisionError:
            answer = list(map(lambda x: mult if x == 0 and nums.count(0) == 1 else 0, nums))
        return answer
