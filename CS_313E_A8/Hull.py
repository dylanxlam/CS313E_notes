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
    '''
    Represents a point in 2D space.

    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
    '''

    def __init__(self, x=0, y=0):
        '''
        Initializes a Point object with optional x and y coordinates.

        Args:
            x (int, optional): The x-coordinate of the point. Defaults to 0.
            y (int, optional): The y-coordinate of the point. Defaults to 0.
        '''
        self.x = x
        self.y = y

    def dist(self, other):
        '''
        Calculate the Euclidean distance between two points.

        Args:
            other (Point): The other point to calculate the distance to.

        Returns:
            float: The Euclidean distance between the two points.
        '''
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        '''
        Returns a string representation of the Point object.

        Returns:
            str: A string in the format "(x, y)" representing the point's coordinates.
        '''
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        '''
        Checks if two Point objects are equal.

        Args:
            other (Point): The other Point object for comparison.

        Returns:
            bool: True if the two points are equal within a tolerance, False otherwise.
        '''
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __lt__(self, other):
        '''
        Compares two Point objects for sorting purposes (based on x-coordinates).

        Args:
            other (Point): The other Point object for comparison.

        Returns:
            bool: True if self is less than other based on x-coordinates, or False otherwise.
        '''
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

def det(p, q, r):
    '''
    Calculate the determinant of three points p, q, and r.

    Args:
        p (Point): The first point.
        q (Point): The second point.
        r (Point): The third point.

    Returns:
        float: The determinant value.
    '''
    return (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x)

def convex_hull(sorted_points):
    '''
    Computes the convex hull of a list of sorted Point objects.

    Args:
        sorted_points (list): A list of Point objects sorted by x-coordinates.

    Returns:
        list: A list of Point objects representing the vertices of the convex hull.
    '''
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
    
    convex_hull = upper_hull + lower_hull
    return convex_hull

def area_poly(convex_poly):
    '''
    Computes the area of a convex polygon defined by a list of Point objects.

    Args:
        convex_poly (list): A list of Point objects representing the convex polygon.

    Returns:
        float: The area of the convex polygon.
    '''
    det_sum = 0
    n = len(convex_poly)
    for i in range(n):
        det_sum += convex_poly[i].x * convex_poly[(i+1) % n].y
        det_sum -= convex_poly[i].y * convex_poly[(i+1) % n].x
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
    
    # Print the vertices of the convex hull
    print("Convex Hull")
    for point in convex_hull_points:
        print(point)
    
    area = area_poly(convex_hull_points)
    print("\nArea of Convex Hull =", area)

if __name__ == "__main__":
    main()
