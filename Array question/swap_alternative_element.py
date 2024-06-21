def SwapAlternativeElement(array):
    first = 0
    second = 1
    while first < len(array)-1 and second < len(array) :
        array[first],array[second] = array[second],array[first]
        first += 2 
        second += 2
    return array
odd_array = [1,2,7,8,5]
even_array = [1,2,3,4,5,6]
print(SwapAlternativeElement(odd_array))
print(SwapAlternativeElement(even_array))