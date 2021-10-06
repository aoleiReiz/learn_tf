def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals = sorted(intervals, key=lambda x:x[0])
    ans = []
    if intervals:
        cur_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] > cur_interval[1]:
                ans.append(cur_interval)
                cur_interval = intervals[i]
            else:
                cur_interval[1] = max(cur_interval[1], intervals[i][1])
        ans.append(cur_interval)
    return ans

