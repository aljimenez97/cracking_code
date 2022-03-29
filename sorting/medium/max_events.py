# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

# You are given an array of events where events[i] = [startDayi, endDayi]. 
# Every event i starts at startDayi and ends at endDayi.

# You can attend an event i at any day d where startTimei <= d <= endTimei. 
# You can only attend one event at any time d.

# Return the maximum number of events you can attend.

import heapq
from os import WUNTRACED

def maxEvents(events):
    events.sort(reverse= True)
    min_heap = []
    res = 0
    max_days = max(events, key= lambda x: x[1])[1]

    for d in range(1, max_days + 1):
        while min_heap and min_heap[0] == d - 1:
            heapq.heappop(min_heap)
        while events and events[-1][0] == d:
            heapq.heappush(min_heap, events[-1][1])
            events.pop()
        
        if not min_heap:
            continue
            
        heapq.heappop(min_heap)
        res += 1
    
    return res
        


if __name__ == "__main__":
    events= [[1,2],[2,3],[3,4],[1,2]]
    print(maxEvents(events))