class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target < nums[0]: return 0
        elif target > nums[-1]: return len(nums)
        else:
            lower, upper = 0, len(nums)-1
            mid = int((lower + upper) / 2)
            while nums[mid] != target:
                if nums[mid] < target:
                    lower = mid
                else:
                    upper = mid
                new_mid = int((lower + upper) / 2)
                if new_mid == mid: return mid+1
                else: mid = new_mid
            return mid