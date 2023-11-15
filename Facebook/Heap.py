# 973. K Closest Points to Origin
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
class K_Closest_Points_to_Origin:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(k):
            heap.append((-math.sqrt(points[i][0] ** 2 + points[i][1] ** 2), points[i]))
        heapq.heapify(heap)

        for i in range(k, len(points)):
            if -math.sqrt(points[i][0] ** 2 + points[i][1] ** 2) > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-math.sqrt(points[i][0] ** 2 + points[i][1] ** 2), points[i]))

        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans

# 253. Meeting Rooms II
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
class Meeting_Rooms_II:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []

        for i in intervals:
            if heap and i[0] >= heap[0]:
                heapq.heapreplace(heap, i[1])
            else:
                heapq.heappush(heap, i[1])

        return len(heap)
