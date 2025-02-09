class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numscopy = nums.copy()
        numsin = []
        for i in numscopy:
            # print(i)
            if i in numsin:
                nums.remove(i)
                # print(nums)
            numsin.append(i)
        return len(nums)
