class Solution:
    def isHappy(self, n: int) -> bool:
        def get_netxt(number):
            return sum(int(digit) ** 2 for digit in str(number))
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1 # 1 이거나 seen에 있으면 빠져나옴
        
