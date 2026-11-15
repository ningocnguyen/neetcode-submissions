"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # min rooms required = max concurrent meetings
        # sol 1: sort
        n = len(intervals)
        i,j = 0, 0
        curr = 0
        min_room = 0
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        while i<n and j<n:
            if starts[i] < ends[j]:
                curr += 1
                min_room = max(min_room, curr)
                i+=1
            else:
                curr -= 1
                j+=1
        
        return min_room