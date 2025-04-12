class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        min_length = len(strs[0])
        do_break = False

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        for i in range(min_length):
            compare = strs[0][i]
            for s in strs:
                if s[i] != compare:
                    do_break = True
                    break
            if do_break:
                break
                
            common_prefix += compare

        return common_prefix
                