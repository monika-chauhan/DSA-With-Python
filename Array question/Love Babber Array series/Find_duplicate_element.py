'''Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2'''

def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break 
    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    return slow 

nums = [1,3,4,2,2]
print(find_duplicate(nums))