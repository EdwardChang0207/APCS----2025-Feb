def f(x):
    if x < 0: return False
    nums = []
    while x >= 10:
        nums.append(x%10)
        x = int(x/10)
    nums.append(x%10)
    for i in range(int(len(nums)/2)):
        if nums[i] != nums[len(nums)-1-i]:
            return False
    return True

print(f(121))