class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Return the two integers in the array that sum to a target integer, in ascending order
        numSet = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in numSet.keys():
                return [numSet[complement], index]
            
            if not number in numSet:
                numSet[number] = index
        return None
