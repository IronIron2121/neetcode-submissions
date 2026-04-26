class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orderedDict = {}

        for string in strs:
            orderedString = "".join(sorted(string))
            if orderedString in orderedDict.keys():
                orderedDict[orderedString].append(string)
            else:
                orderedDict[orderedString] = [string]

        
        return list(orderedDict.values())