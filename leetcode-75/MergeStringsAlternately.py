# 0 pointers

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n = len(word1)
        m = len(word2)
        
        # make sure every char is added -> max
        for idx in range(max(n, m)):
            if idx < n:
                res.append(word1[idx])
            if idx < m:
                res.append(word2[idx])

        return "".join(res)

        
