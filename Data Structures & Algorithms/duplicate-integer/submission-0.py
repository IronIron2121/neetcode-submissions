class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, val in enumerate(nums):
            checkIndex = index + 1
            while checkIndex < len(nums):
                if nums[checkIndex] == val:
                    return True
                checkIndex += 1


        return False