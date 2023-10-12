nums = input() 
result = any(nums.count(x) > 1 for x in nums)
print(result)
