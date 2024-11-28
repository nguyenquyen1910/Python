from shapely.geometry import Polygon
from shapely.ops import unary_union


def dien_tich_che_phu(n, triangles):
    polygons = []
    for triangle in triangles:
        polygons.append(
            Polygon(
                [
                    (triangle[0], triangle[1]),
                    (triangle[2], triangle[3]),
                    (triangle[4], triangle[5]),
                ]
            )
        )

    union = unary_union(polygons)
    return round(union.area, 6)


n = int(input())
triangles = []
for _ in range(n):
    triangles.append(list(map(int, input().split())))

result = dien_tich_che_phu(n, triangles)
print(f"{result:.6f}")
