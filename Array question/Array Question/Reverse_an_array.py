def reverse_array(array):
    start = 0 
    right = len(array)-1
    while start < right:
        array[start],array[right] = array[right],array[start]
        start += 1
        right -= 1
    return array 
array = [2,3,4,5,6]
print(reverse_array(array))
