'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''

def merge_intervals(intervals):
    intervals.sort(key = lambda x : x[0])
    merge = [intervals[0]]
    for i in range(1,len(intervals)):
        if merge[-1][1] < intervals[i][0]:
            merge.append(intervals[i])
        else:
            merge[-1][1] = max(merge[-1][1],intervals[i][1])
    return merge 

intervals = [[1,4],[0,4]]
intervals_2 = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))
print(merge_intervals(intervals_2))