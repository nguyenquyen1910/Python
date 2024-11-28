def find_circle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if d == 0:
        return None, None

    h = (
        (x1**2 + y1**2) * (y2 - y3)
        + (x2**2 + y2**2) * (y3 - y1)
        + (x3**2 + y3**2) * (y1 - y2)
    ) / d
    k = (
        (x1**2 + y1**2) * (x3 - x2)
        + (x2**2 + y2**2) * (x1 - x3)
        + (x3**2 + y3**2) * (x2 - x1)
    ) / d

    r2 = (x1 - h) ** 2 + (y1 - k) ** 2
    return (h, k), r2


def count_points_inside(circle, radius2, points, excluded_points):
    cx, cy = circle
    count = 0
    for x, y in points:
        if (x, y) in excluded_points:
            continue
        distance2 = (x - cx) ** 2 + (y - cy) ** 2
        if distance2 < radius2:
            count += 1
    return count


def solve_test_case(n, k, points):
    for i in range(n):
        for j in range(i + 1, n):
            for l in range(j + 1, n):
                p1, p2, p3 = points[i], points[j], points[l]

                circle, radius2 = find_circle(p1, p2, p3)
                if circle is None:
                    continue

                inside_count = count_points_inside(
                    circle, radius2, points, {p1, p2, p3}
                )

                if inside_count == k:
                    return "YES"
    return "NO"


def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        k = int(input())
        points = [tuple(map(int, input().split())) for _ in range(n)]
        results.append(solve_test_case(n, k, points))
    print(*results, sep="\n")


if __name__ == "__main__":
    main()
