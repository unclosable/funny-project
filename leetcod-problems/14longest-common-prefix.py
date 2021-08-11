class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        
        for i in range(len(strs[0])):
            s = strs[0][i]
            brea = False
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != s:
                    brea = True
                    break
            if brea: break
            pre += s
        return pre
