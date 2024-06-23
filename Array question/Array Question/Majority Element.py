'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

def majorityElement(nums):
    d = {}
    n = len(nums)
    for i in nums:
        d[i] = d.get(i,0) + 1
    
    for key in d.keys():
        if d[key] > n // 2:
            return key 
    return -1 

nums = [2,2,2,1,1,1,2,2]
print(majorityElement(nums)) 
        