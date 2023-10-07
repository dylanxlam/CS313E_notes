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
import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __le__(self, other):
        if self.x == other.x:
            return self.y <= other.y
        return self.x <= other.x

    # Add other comparison methods (__ne__, __gt__, __ge__) here.

# Rest of the code remains the same...


def det(p, q, r):
    return (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x)

def convex_hull(sorted_points):
    upper_hull = [sorted_points[0], sorted_points[1]]
    
    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) < 0:
            del upper_hull[-2]
    
    lower_hull = [sorted_points[-1], sorted_points[-2]]
    
    for i in range(len(sorted_points) - 3, -1, -1):
        lower_hull.append(sorted_points[i])
        while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) < 0:
            del lower_hull[-2]
    
    # Remove first and last points from lower hull to avoid duplication
    lower_hull.pop(0)
    lower_hull.pop(-1)
    
    # Combine upper and lower hulls to form the convex hull
    convex_hull = upper_hull + lower_hull
    return convex_hull

def area_poly(convex_poly):
    # Compute and return the area of a convex polygon
    det_sum = 0
    n = len(convex_poly)
    for i in range(n):
        det_sum += convex_poly[i].x * convex_poly[(i + 1) % n].y
        det_sum -= convex_poly[i].y * convex_poly[(i + 1) % n].x
    area = 0.5 * abs(det_sum)
    return area

def main():
    points_list = []
    
    num_points = int(sys.stdin.readline().strip())
    
    for i in range(num_points):
        line = sys.stdin.readline().strip().split()
        x, y = int(line[0]), int(line[1])
        points_list.append(Point(x, y))
    
    sorted_points = sorted(points_list)
    
    convex_hull_points = convex_hull(sorted_points)
    
    # Find the index of the leftmost and bottommost point (starting point)
    start_idx = sorted_points.index(convex_hull_points[0])
    
    # Print the vertices of the convex hull in the desired order
    for i in range(len(convex_hull_points)):
        idx = (start_idx + i) % len(convex_hull_points)
        print(convex_hull_points[idx])
    
    area = area_poly(convex_hull_points)
    print("\nArea of Convex Hull =", area)


if __name__ == "__main__":
    main()

