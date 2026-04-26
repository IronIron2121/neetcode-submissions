class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for string in strs:
            outDictionary = {char: 0 for char in alphabet}
            
            for char in string:
                outDictionary[char] += 1
            
            key = tuple(outDictionary.values())

            if key in keys:
                keys[key].append(string)
            else:
                keys[key] = [string]

        return list(keys.values())