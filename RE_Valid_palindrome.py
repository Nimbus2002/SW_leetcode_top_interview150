class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 내 풀이
        # alphanumeric = "".join([char.lower() for char in s if char.isalnum()])
        # # print("1".lower())  # 숫자는 lower해도 그대로임
        # return alphanumeric == alphanumeric[::-1]

        # two pointer풀이
        i, j = 0, len(s)-1 # 앞에서 부터, 뒤에서 부터
        while i<j: # 만날때까지
            while i<j and not s[i].isalnum(): i +=1 
            while i < j and not s[j].isalnum(): j -= 1

            if s[i].lower() != s[j].lower(): return False
            i +=1
            j -= 1

        return True
