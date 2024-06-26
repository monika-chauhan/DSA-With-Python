'''Given an array arr of size n and an integer x. Find if there's a triplet in the array which sums up to the given integer x.

Examples

Input:n = 6, x = 13, arr[] = [1,4,45,6,10,8]
Output: 1
Explanation: The triplet {1, 4, 8} in the array sums up to 13.
'''


def find3Numbers(arr,n,x):
    arr.sort()
    for i in range(n-2):
        j = i + 1
        k = n - 1
        while j < k:
            sum = arr[i]+arr[j]+arr[k]
            if sum == x:
                return True 
            elif sum > x:
                k -= 1
            else:
                j += 1
    return False 
arr = [1,2,4,3,6,7]
n = 5
x = 10
print(find3Numbers(arr,n,x))