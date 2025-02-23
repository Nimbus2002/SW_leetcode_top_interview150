class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle in haystack: #존재 하지 않으면
            return -1
        else: # 존재하면
            return haystack.find(needle)



# find안쓰는 방법
    def strStr2(self, haystack: str, needle: str) -> int:
        len_h = len(haystack)
        len_n = len(needle)
        for i in range(len_h - len_n + 1):
            equal = True
            for j in range(len_n):
                if haystack[i+j] != needle[j]:
                    equal = False
                    break
            if equal == True:
                return i
        return -1
