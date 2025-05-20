def non_overlapping(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for current in intervals[1:]:
        prev = result[-1]
        # print (prev)

        if current[0] <= prev[1]:
            print(f"current if {current}")
            prev[1] = max(prev[1], current[1])
        else:
            print(f"current else {current}")
            result.append(current)

    return result



print(non_overlapping([[1,2],[2,3],[3,4],[1,3]]))
print(non_overlapping([[1,3], [2, 6], [8, 10], [11,12]]))
