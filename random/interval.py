# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return str(tuple([self.start, self.end]))

class Node(object):
    def __init__(self, v = 0):
        self.val = v
        self.l = None
        self.r = None
    def insert(self, v):
        if v == self.val:
            return
        if v <= self.val:
            if self.l == None:
                self.l = Node(v)
            else:
                self.l.insert(v)
        else:
            if self.r == None:
                self.r = Node(v)
            else:
                self.r.insert(v)

def go_to_close(node):
    if node.l != None:
        if node.r == None:
            return node
        else:
            return go_to_close(node.r)
    else:
        return node

class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return [intervals[0]]

        intervals.sort(key=lambda x: (x.start, x.end))

        meetings = [intervals[0]]
        for curr in intervals[1:]:
            curr_start, curr_end = curr.start, curr.end

            last_end = meetings[-1].end
            if curr_start <= last_end and curr_end >= last_end:
                meetings[-1] = Interval(meetings[-1].start, curr_end)
            else:
                meetings.append(curr)
        return meetings

    def merge2(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return [intervals[0]]

        root = Node()
        entry = intervals[0]
        root.val = entry.start
        root.insert(entry.end)

        # O(n^2) == O(n) outer * O(2n) insertion worst case
        for val in intervals[1:]:
            v1, v2 = val.start, val.end
            root.insert(v1)
            root.insert(v2)

        # Merge the intervals together
        merged = []
        curr = root

        while curr != None and not (curr.l == None and curr.r == None):
            head = curr
            curr = curr.r

            if curr != None:
                tail = go_to_close(curr)
            else:
                tail = head

            merged.append([head.val, tail.val])

            curr = tail.r

        return merged


# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,3]]
intervals = [[2,3],[5,5],[2,2],[3,4],[3,4]]
intervals = map(lambda l : Interval(l[0], l[1]), intervals)
s = Solution()
print s.merge(intervals)
