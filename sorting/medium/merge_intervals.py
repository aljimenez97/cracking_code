# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping 
# intervals that cover all the intervals in the input.

def merge_intervals(intervals):
    intervals.sort(key= lambda x: x[0])

    out = [intervals[0]]

    for starti, endi in intervals[1:]:
        if starti <= out[-1][1]:
            out[-1] = [out[-1][0], max(endi, out[-1][1])]
        else:
            out.append([starti, endi])
    return out

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge_intervals(intervals))