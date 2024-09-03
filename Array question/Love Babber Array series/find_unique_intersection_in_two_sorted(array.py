def unionIntersection(a1,a2):
    i = 0 
    j = 0 
    intersection = []
    union = []
    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            intersection.append(a1[i])
            union.append(a1[i])
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            union.append(a1[i])
            i += 1
        else:
            union.append(a2[j])
            j += 1
    while i < len(a1):
        union.append(a1[i])
        i += 1
    while j < len(a2):
        union.append(a2[j])
        j += 1
    return intersection,union

a1 = [1,2,3,4,5,6,7,8]
a2 = [3,5,7]
print(unionIntersection(a1,a2))