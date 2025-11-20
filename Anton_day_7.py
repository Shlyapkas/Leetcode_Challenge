class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        prefix = 1
        for index in range(len(nums)):

            result.insert(index, prefix)
            prefix *= nums[index]

        suffix = 1
        for index in range(1, len(nums) + 1):
            result[-index] *= suffix
            suffix *= nums[-index]

        return result






Input = [1,2,3,4]
# Output: [24,12,8,6]



# Input = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


sol = Solution()
print(sol.productExceptSelf(Input))