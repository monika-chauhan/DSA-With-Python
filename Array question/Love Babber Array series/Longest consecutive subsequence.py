'''Given an array of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
Example 1:

Input:
N = 7
a[] = {2,6,1,9,4,5,3}
Output:
6
Explanation:
The consecutive numbers here
are 1, 2, 3, 4, 5, 6. These 6 
numbers form the longest consecutive
subsquence.
'''
'''Approach: temp =[0]*(max(arr)+1)
i   arr[i]     temp[i]                  count       Long_subsequence
0     2      [0,0,1,0,0,0,0,0,0,0]       1             1
1     6      [0,0,1,0,0,0,1,0,0,0]       1             1
2     1      [0,1,1,0,0,0,1,0,0,0]       2             2
3     9      [0,1,1,0,0,0,1,0,0,1]       2             2
4     4      [0,1,1,0,1,0,1,0,0,1]       2             2
5     5      [0,1,1,0,1,1,1,0,0,1]       3             3
6     3      [0,'1,1,1,1,1,1',0,0,1]       6             5

'''

def LongestConsecutiveSubSequence(arr,n):
    long_subseq = float('-inf') 
    count = 0 
    temp = [0] * (max(arr)+1)
    for i in range(n):
        temp[arr[i]] = 1
    
    for i in range(len(temp)):
        if temp[i] == 1:
            count += 1
            long_subseq = max(long_subseq,count)
        else:
            count = 0 
    return long_subseq

arr = [2,6,1,9,4,5,3]
n = len(arr) 
print(LongestConsecutiveSubSequence(arr,n))


### Second Approach

def Longest_consecutive_subsequence(arr,n):
    s = set() 
    ans = float('-inf')
    for i in arr:
        s.add(i)

    for i in range(n):
        if (arr[i]-1) not in s: 
            j=arr[i] 
            #then we keep checking whether the next consecutive elements
            #are present in Set and we keep incrementing the counter. 
            while(j in s): 
                j+=1
            #storing the maximum count.
            ans=max(ans, j-arr[i]) 
    return ans
arr = [2,6,1,9,4,5,3]
n = len(arr) 
print(Longest_consecutive_subsequence(arr,n))