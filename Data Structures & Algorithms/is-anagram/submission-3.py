class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ 
        - create a set of S
        - for each character in t:
            pop that character from S
            IF the character is not in S
                return false

        return true
        """

        if len(s) != len(t):
            return False

        newDict = {char : s.count(char) for char in s}        

        oldSize = 0

        for char in t:
            if char not in newDict or newDict[char] <= 0:
                return False

            newDict[char] -= 1
            
        return True