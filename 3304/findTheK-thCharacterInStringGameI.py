class Solution:
    def kthCharacter(self, k: int, word = 'a') -> str:
        for i in range(len(word)):
            word += chr(ord(word[i]) + 1)

        try:
            return word[k - 1]
        except:
            return self.kthCharacter(k, word)