class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = "" # 기본은 빈칸
        strs = sorted(strs) # 비교하기 쉽게
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans+=first[i]
        return ans
