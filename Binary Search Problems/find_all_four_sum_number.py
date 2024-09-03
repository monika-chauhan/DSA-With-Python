'''Given an array A of integers and another number K. Find all the unique quadruple from the given array that sums up to K.

Also note that all the quadruples which you return should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.

Example 1:

Input:
N = 5, K = 3
A[] = {0,0,2,1,1}
Output: 0 0 1 2 
Explanation: Sum of 0, 0, 1, 2 is equal
to K.'''

def fourSum(arr,k):
    n = len(arr)
    res = []
    if n < 4:
        return res 
    for i in range(n-3):
        if i > 0 and arr[i] > k:
            break 
        if i > 0 and arr[i] == arr[i-1]:
            continue 

        for j in range(i+1,n-2):
            if j > i + 1 and arr[j] == arr[j-1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                old_l = left 
                old_r = right 
                sum = arr[i] + arr[j] + arr[left] + arr[right]

                if sum == k:
                    res.append([arr[i],arr[j],arr[left],arr[right]])
                    while left < right and arr[left] == arr[old_l]:
                        left += 1
                    while left < right and arr[right] == arr[old_r]:
                        right -= 1
                elif sum > k:
                    right -= 1
                else:
                    left += 1
    return res 
arr = [10,2,3,4,5,7,8]
k = 23 
print(fourSum(arr,k))