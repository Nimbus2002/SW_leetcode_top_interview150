class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 
        repeat = 0
        for i in range(1, len(nums)):
            #다르면 추가
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k +=1
                repeat =0
            # 같으면 체크
            else:
                repeat+=1
                if repeat == 1:
                    nums[k] = nums[i]
                    k +=1
        return k
