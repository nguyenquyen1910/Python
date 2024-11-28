import math
from collections import defaultdict

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] += val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node]  + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if start > right or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(2 * node, start, mid, left, right) + self.query(2 * node + 1, mid + 1, end, left, right) 
def angle(p1, p2):
    """Tính góc của p2 so với p1."""
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def check_circle(points, k):
    n = len(points)
    for i in range(n):
        angles = []
        for j in range(n):
            if i != j:
                angles.append(angle(points[i], points[j]))
        angles.sort()
        angles += [a + 2 * math.pi for a in angles]  # Thêm các góc + 2pi

        tree = SegmentTree(2 * n)
        count = defaultdict(int)
        for j in range(n):
            if i != j:
                count[angles[j]] += 1
                tree.update(1, 0, 2 * n - 1, j, 1)

        for j in range(n):
            if i != j:
                left = j
                right = j + n - 1
                num_points = tree.query(1, 0, 2 * n - 1, left, right) - count[angles[j]]
                if num_points == k:
                    return True
                tree.update(1, 0, 2 * n - 1, j, -1)
                tree.update(1, 0, 2 * n - 1, j + n, -1)
    return False

# Đọc số lượng bộ test
T = int(input())

for _ in range(T):
    # Đọc input cho mỗi test
    n=int(input())
    k=int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    # Kiểm tra và in kết quả
    if check_circle(points, k):
        print("YES")
    else:
        print("NO")
