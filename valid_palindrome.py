class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "".join([char.lower() for char in s if char.isalnum()])
        # print("1".lower())  # 숫자는 lower해도 그대로임
        return alphanumeric == alphanumeric[::-1]
