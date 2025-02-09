class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if not i in a:
                a[i] =1
            else:
                a[i]+=1
        # print(a)
        maxnum =0
        ans = 0 
        for key in a:
            if maxnum < a[key]:
                maxnum =a[key]
                ans = key
        return ans

## 더 좋음
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
