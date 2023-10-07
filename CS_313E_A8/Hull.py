#  File: Hull.py

#  Description: Python program that employs the Graham's scan algorithm to determine the convex 
    # hull of a set of 2D points. It reads input points, calculates the convex hull, and prints 
    # the vertices of the convex hull along with its area. The code also includes a Point class to 
    # manage 2D points and maintains the clockwise order of convex hull vertices.

#  Student Name: Dylan Lam

#  Student UT EID: DXL85

#  Partner Name: Alexander Romero-Barrionuevo

#  Student's UT EID: ANR3784 

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created: 10/3/2023

#  Date Last Modified: 10/6/2023

import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def convex_hull(points):
    points.sort(key=lambda p: (p.x, p.y))  # Sort points lexicographically
    lower = []
    upper = []

    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    return lower[:-1] + upper[:-1]  # Combine lower and upper hulls (exclude duplicates)

def area_of_polygon(polygon):
    n = len(polygon)
    if n < 3:
        return 0.0

    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i].x * polygon[j].y
        area -= polygon[i].y * polygon[j].x

    area = abs(area) / 2.0
    return area

def main():
    n = int(sys.stdin.readline())
    points_list = []

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        points_list.append(Point(x, y))

    hull = convex_hull(points_list)
    hull.sort(key=lambda p: (p.x, p.y))  # Sort points in convex hull lexicographically

    print("Convex Hull")
    for point in hull:
        print(f"({point.x}, {point.y})")

    hull_area = area_of_polygon(hull)
    print(f"\nArea of Convex Hull = {hull_area:.1f}")

if __name__ == "__main__":
    main()
