class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        create an empty dictionary
        for each string in list:
            order the string
            IF it already exists in the dictionary:
                add it to list at that key
            ELSE:
                dictionary[orderedString] = string
        """
        orderedDict = {}

        for string in strs:
            orderedString = "".join(sorted(string))
            if orderedString in orderedDict.keys():
                orderedDict[orderedString].append(string)
            else:
                orderedDict[orderedString] = [string]

        
        return list(orderedDict.values())