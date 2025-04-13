class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        indexs = [0] * 200
        indext = [0] * 200
        
        length = len(s)

        if length != len(t):
            return False
        for i in range(length):
            if indexs[ord(s[i])] != indext[ord(t[i])]:
                return False
            indexs[ord(s[i])] = i + 1
            indext[ord(t[i])] = i + 1

        return True
        
