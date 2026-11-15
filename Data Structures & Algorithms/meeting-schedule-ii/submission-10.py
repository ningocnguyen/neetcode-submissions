"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # min heap to store earliest ending time
        # iterate through intervals to evaluate meeting start time
        # if start time starts after the earliest meeting end time --> pop from heap (meeting can be reused)
        heap = []
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        heapq.heappush(heap, intervals[0].end)

        for interval in intervals[1:]:
            if interval.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)

        return len(heap)