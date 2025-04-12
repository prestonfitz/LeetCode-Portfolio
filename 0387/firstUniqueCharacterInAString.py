class Solution:
    def subset(self, s: str) -> str:
        count = s.count(s[0])
        if count == 1:
            return s[0]
            
        t = s.replace(s[0], "")

        if len(t) > 0:
            return self.subset(t)
        else:
            return ""

    def firstUniqChar(self, s: str) -> int:
        char = self.subset(s)

        if char != "":
            return s.index(char)
        else:
            return -1
        
