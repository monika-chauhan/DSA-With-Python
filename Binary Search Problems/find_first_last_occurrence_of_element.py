# binary search we are applying
def firstOccur(arr,x):
    left = 0 
    right = len(arr) - 1
    ans = -1
    while left <= right:
        mid = left+(right - left) // 2
        if arr[mid] == x:
            ans = mid 
            right = mid - 1 # we have to check if the left part contains the element of not so minimize the search space
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return ans 

def lastOccur(arr,x):
    left = 0 
    right = len(arr) - 1
    ans = -1
    while left <= right:
        mid = left+(right - left) // 2
        if arr[mid] == x:
            ans = mid 
            left = mid + 1 # we have to check if the right part contains the element of not so minimize the search space
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return ans 

def findOccurrence(arr,x):
    first = firstOccur(arr,x)
    last = lastOccur(arr,x)
    return [first,last]


def total_occurrence(arr,x):
    first = firstOccur(arr,x)
    last = lastOccur(arr,x)
    return last - first + 1

arr = [1,2,3,3,3,3,4]
x = 3 
print(f"The first and Last occurence of {x}element: {findOccurrence(arr,x)}")
print(f"Total number of occurrence of {x} element is :{total_occurrence(arr,x)}")