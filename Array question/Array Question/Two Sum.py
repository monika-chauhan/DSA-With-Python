'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''Logic: create a hashMap that store the remaining resule by subtracting the number
from target else store the number with index {num:index} if not present in hashMap
1) 9 - 2 => 5 not in hashMap then hashMap = {2:0}
2) 9 - 7 => 2 yes in HashMap then return (hashMap[target-number], index) as result
'''

def TwoSum(nums,target):
    hashMap = {}
    for i, val in enumerate(nums):
        if target - val in hashMap:
            return hashMap[target-val],i 
        hashMap[val] = i 
    return -1 

nums = [2,7,11,15]
target = 9 
print(TwoSum(nums, target))