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

        # The key thing is that you place your information at the BEGINNING of string
        # This way...how do I articulate this?
        # You are basically putting the decoding instructions at the start
        # Any attempt to use actual delimiters will be open to being misunderstood for the actual string being decoded
        # But if you KNOW that your input comes first, and you have CLEAR RULES for how that input is written,
        # It becomes a lot clearer how to decipher the string that follows
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

        index += 1
        index2 = 0
        while index2 < len(sizes):
            out.append(s[index : index + sizes[index2]])
            index = index + sizes[index2]
            index2+=1

        return out