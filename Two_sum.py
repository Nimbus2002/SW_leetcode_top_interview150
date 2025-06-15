class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        # solution (1) brute force
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        # # solution (2) - hasp map즉, dic에서 key찾는건 o(1)
        # nummaps ={}
        # n = len(nums)

        # for i in range(n):
        #     nummaps[nums[i]] = i 

        # for i in range(n):
        #     complement = target - nums[i]
        #     if complement in nummaps and nummaps[complement] != i:
        #         return [i, nummaps[complement]]

        # return []
        # solution 3 - one pass hash table
        nummap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in nummap:
                return [nummap[complement], i]
            nummap[nums[i]] = i 

        return []
