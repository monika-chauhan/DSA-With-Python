# Get the pivot element in array 
def getPivot(array):
    left = 0 
    right = len(array) - 1 
    while left < right:
        mid = left + (right - left)//2
        print('m',mid)
        if array[0] <= array[mid]:
            left = mid + 1
            print('l',left)
        else:
            right = mid
            print('r',right) 
    return left

array = [7,9,1,2,3]
print(getPivot(array)) 
