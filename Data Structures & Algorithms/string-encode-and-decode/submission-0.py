class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        encoded_string = "".join(res)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        x = 0

        while x < len(s):
            y = x
            while s[y] != '#':
                y += 1
            length = int(s[x:y])
            x = y + 1
            y = x + length
            res.append(s[x:y])
            x = y
        return res