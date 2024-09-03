'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
'''

'''Logic :-> as per the ^ (xor operator) if one number is repeated twice then the xor of number is 0 
2 ^ 2 => 0 (010 ^ 010 => 000)'''
def single_number(nums):
    xor = 0 
    for i in nums:
        xor ^= i 
    return xor 

nums = [2,2,1]
print(single_number(nums))