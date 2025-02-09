class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        numscopy = nums.copy()
        n = len(nums)
        if k >= n:
            k  = k - (k//n) * n
        nums[k:] = numscopy[0:n-k]
        nums[0:k] = numscopy[n-k:]
