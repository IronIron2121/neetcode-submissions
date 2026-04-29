class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        out = ""
        sizes = []
        for string in strs:
            sizes.append(len(string))
        for size in sizes:
            out += str(size)
            out += ';'
        out += '#'
        for string in strs:
            out += string
 
        return out

    def decode(self, s: str) -> List[str]:
        if not s:
            print('No S')
            return []

        out = []
        sizes = []
        char = ''
        index = 0
        char = s[index]
        
        while char != '#':
            thisSize = ''

            while char != ';':
                thisSize += char
                index += 1
                char = s[index]

            sizes.append(int(thisSize))
            index += 1
            char = s[index]

        
        strStart = sum(sizes)
        print(sizes)
        print(strStart, s)

        index += 1
        index2 = 0
        while index2 < len(sizes):
            out.append(s[index : index + sizes[index2]])
            index = index + sizes[index2]
            index2+=1

        return out