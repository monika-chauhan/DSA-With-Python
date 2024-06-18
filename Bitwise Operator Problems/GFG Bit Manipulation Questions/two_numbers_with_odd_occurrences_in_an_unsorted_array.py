'''Given an unsorted array that contains even number of occurrences for all numbers except two numbers. Find the two numbers which have odd occurrences in O(n) time complexity and O(1) extra space.

Examples: 

Input: {12, 23, 34, 12, 12, 23, 12, 45}
Output: 34 and 45

Input: {4, 4, 100, 5000, 4, 4, 4, 4, 100, 100}
Output: 100 and 5000

Input: {10, 20}
Output: 10 and 20
'''

def TwoOddNumber(Arr):
    xor = 0 
    for num in Arr:
        xor = xor ^ num

    #finding the rightmost set bit in xor2
    set_bit_no = xor & ~(xor-1) 
    
    x,y = 0, 0 
    #finding the first odd occurring number (x) and the second odd occurring number (y)   
    for i in range(len(Arr)):
        if Arr[i] & set_bit_no:
            x = x ^ Arr[i]
        else:
            y = y ^ Arr[i]
    
    #returning the max and min values of x and y as a list
    v = [max(x, y), min(x, y)]
    return v
print(TwoOddNumber([12,23,34,12,12,23,12,45]))
