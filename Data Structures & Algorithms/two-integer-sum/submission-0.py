class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print("Entered")
        # Return the two integers in the array that sum to a target integer, in ascending order
        for index, num in enumerate(nums):
            rightPointer = index + 1
            while rightPointer < len(nums):
                summed = num + nums[rightPointer]
                if summed == target:
                    return [index, rightPointer]
                rightPointer += 1
