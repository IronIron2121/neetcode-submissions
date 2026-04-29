class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefs = []
        posts = []
        
        prod = 1

        # create prefix array
        for num in nums:
            prod *= num
            prefs.append(prod)

        nums = list(reversed(nums))

        # create post fix array
        prod = 1
        for num in nums:
            prod *= num
            posts.append(prod)


        posts = list(reversed(posts))

        for index in range(len(prefs)):
            if index == 0:
                res.append(posts[index+1] * 1)
            elif index == (len(prefs) - 1):
                print(prefs[index])
                res.append(prefs[index-1] * 1)
            else:
                res.append(prefs[index-1] * posts[index + 1])
        return res
