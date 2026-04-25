class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for index, val in enumerate(nums):
            if val in hashSet:
                return True
            hashSet.add(val)


        return False