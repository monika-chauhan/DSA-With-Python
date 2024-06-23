'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.'''


'''Logic -> Calculate the total number by using formula n*(n+1)//2 for n number then sum of given array element
n = 3 then totalSum = 3*(3+1)//2 => 6 and nums_sum = 3+0+1=> 4 then answer=> 6 - 4 = 2  '''
def missing_number(nums):
    n = len(nums)
    total_sum = n*(n+1)//2  # total sum of range(n)
    nums_sum = 0 
    for i in nums:
        nums_sum += i 
    
    return total_sum - nums_sum 

nums = [3,0,1]
print(missing_number(nums))