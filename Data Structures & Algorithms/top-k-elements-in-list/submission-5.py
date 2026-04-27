class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sort the list
        sortedList = sorted(nums)
        # Create empty dictionary to hold number occurences
        counts = {}
        # Create empty buckets to store frequency of occurences
        frequencies = [[] for i in range(len(nums) + 1)]

        # get the counts for every value in the list
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # add the counts to the relevant bucket in our frequency list
        for num, count in counts.items():
            print(count)
            frequencies[count].append(num)

        out = []
        # iterate through in reverse order and only get the relevant buckets (early exit when we have k buckets)
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                out.append(num)
                if len(out) == k:
                    return out
