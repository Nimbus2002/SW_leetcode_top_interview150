class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = {
            'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }

        result = 0 
        for i in range(len(s)-1):
            if roman2int[s[i]] < roman2int[s[i + 1]]:
                result -= roman2int[s[i]]
            else:   
                result += roman2int[s[i]]
        result += roman2int[s[-1]]
        return result
