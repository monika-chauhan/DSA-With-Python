'''Given an array arr[] of size n of non-negative integers. Each array element represents the maximum length of the jumps that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0, then you cannot move through that element.
Note:  Return -1 if you can't reach the end of the array.

Examples : 

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}, n = 11
Output: 3 
Explanation:First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 
Input: arr = {1, 4, 3, 2, 6, 7}, n = 6
Output: 2 
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
'''
'''
Approach: max_jump = curr = jumps = 0 
i   a[i]    max_jump/max(max_jump,a[i]+i)    curr= max_jump if (i == curr)       jumps += 1 if (i == curr)
0   1        max(0,a[0]+0) = 1                      1                                   1
1   4        max(1,a[1]+1) = 5                      5                                   2
2   3        max(5,a[2]+2)= 5                  if curr >= n-1 then return jumps = 2  
3   2                                               5>=6-1=5 jumps = 2
4   6
5   7
'''

def min_jumps(arr,n):
    jumps = 0 
    max_jump = 0 
    curr = 0 
    if n == 0 or n == 1:
        return 1 

    if arr[0] == 0:
        return -1 

    for i in range(n):
        max_jump = max(max_jump,arr[i]+i)

        if i == curr:
            jumps += 1
            curr = max_jump

        if curr >= n-1:
            return jumps 
    return -1

arr = [1, 4, 3, 2, 6, 7] 
n = len(arr)
print(min_jumps(arr,n))           
