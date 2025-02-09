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


## 더 좋은 방법
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j +=1
        return j
