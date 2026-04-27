class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create empty dictionary to hold number occurences
        outDict = {}
        for num in nums:
            if num in outDict:
                outDict[num] += 1
            else:
                outDict[num] = 1

        sortedDict = {num : occurrences for num, occurrences in sorted(outDict.items(), key = lambda item: item[1])}

        return (list(sortedDict.keys())[-k:len(sortedDict)])
