'''Approach: arr = [0,1,2,1,0]
assign left = mid = 0 and right = n - 1
while mid <= high:

mid   arr[mid]  left  right         Swap           swap Arr      swap_left  swap_mid     swap_right
0     0         0     n-1    swap(a[mid],a[left])   [0,1,2,1,0]     1          1            n-1
1     1         1     n-1    no swap(inc mid)       [0,1,2,1,0]     1          2            n-1
2     2         1     n-1    swap(a[mid],a[right])  [0,1,0,1,2]     1          2            n-1-1(5-1-1)=3
2     0         1     3      swap(a[mid],a[left])   [0,0,1,1,2]     2          3            3
3     1         1     3      no swap(inc mid)       [0,0,1,1,2]     2          4            3
break as mid = 4 and right = 3 (4 <=3) condition failed 
   ''' 
def sort0s1s2s(array,n):
    left = mid = 0 
    right = n - 1
    while mid <= right:
        if array[mid] == 0:
            array[left],array[mid] = array[mid] ,array[left]
            left += 1
            mid +=1
        
        elif arr[mid] == 1:
            mid += 1
        else:
            array[right],array[mid] = array[mid] ,array[right]
            right -= 1
    return array

arr = [0,1,2,1,2,0]
print(sort0s1s2s(arr, len(arr)))