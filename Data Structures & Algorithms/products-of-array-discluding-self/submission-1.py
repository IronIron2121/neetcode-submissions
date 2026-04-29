class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for index, num in enumerate(nums):
            prod = 1
            for index2, num2 in enumerate(nums):
                if index2 != index:
                    prod *= num2
            res.append(prod)

        return res
