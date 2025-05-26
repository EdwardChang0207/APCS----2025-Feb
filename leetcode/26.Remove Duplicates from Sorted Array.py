def removeDuplicates(nums: list[int]) -> int:
        s = set()
        c = 0
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
        k = len(list(s))
        nums = list(s)
        print(nums)
        return k
print(removeDuplicates(nums=[1,1,2]))