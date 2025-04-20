class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split(" ")

        if len(l) != len(pattern): # 개수가 안맞으면 일단 false
            return False

        d = {}
        se = set()

        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != l[i]:
                    return False
            else:
                if l[i] not in se: # 아직 안본 세트
                    d[pattern[i]] = l[i]
                    se.add(l[i])
                else: # 본 단어인데 pattern은 다를때
                    return False
        return True

 
