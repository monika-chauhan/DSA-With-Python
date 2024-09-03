'''You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
'''

'''Logic -> 
duplicate -> sum(nums) => sum([1,2,2,4]) => 9 and sum(set(nums)) => sum([1,2,4]) => 7 then 9-7 = 2 that is duplicate
missing -> total sum of n number-> n*(n+1)//2 => 4*(4+1)//2=> 10 and sum(set(nums)) => 7 => 10-7= 3
answer=> [2, 3]'''


def findErrorNums(nums):
    n = len(nums)
    duplicate = sum(nums) - sum(set(nums))
    missing = n*(n+1)//2 - sum(set(nums))
    return [duplicate,missing]

nums = [1,2,3,2]
print(findErrorNums(nums))