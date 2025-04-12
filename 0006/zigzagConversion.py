class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == 0:
            return s
        backtrack = False
        index = 1
        rows = {i: "" for i in range(1, numRows + 1)}
        
        for letter in s:
            rows[index] += letter

            if index == numRows:
                backtrack = True
            elif index == 1:
                backtrack = False

            if backtrack:
                index -= 1
            else:
                index += 1

        result = ''

        for i in range(1, numRows + 1):
            result += rows[i]

        return(result)
        