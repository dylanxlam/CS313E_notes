#  File: Geometry.py

#  Description: This program serves as a versatile 
#  geometry utility. It reads input data from a text file, 
#  detailing properties of geometric shapes like points, spheres, 
#  cubes, and cylinders. The program then conducts various 
#  evaluations on these shapes. It determines relationships such 
#  as proximity of points to origins, containment of points within 
#  shapes, inclusion of one shape within another, and intersection 
#  between shapes. The program provides clear and informative responses 
#  to these geometric inquiries, making it a valuable tool for analyzing 
#  spatial configurations.

#  Student Name: Alexander Romero-Barrionuevo

#  Student UT EID: ANR 3784

#  Partner Name: Dylan Lam

#  Partner UT EID: DXL85

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created: 9/17/2023

#  Date Last Modified: 9/17/2023

import math
import sys

class Point(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f}, {self.z:.1f})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def __eq__(self, other):
        return (
            math.isclose(self.x, other.x) and
            math.isclose(self.y, other.y) and
            math.isclose(self.z, other.z)
        )

class Sphere(object):
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

    def __str__(self):
        return f"Center: ({self.x:.1f}, {self.y:.1f}, {self.z:.1f}), Radius: {self.radius:.1f}"

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def is_inside_point(self, p):
        return p.distance(self) < self.radius

    def is_inside_sphere(self, other):
        return self.radius >= other.radius and self.distance(other) + other.radius <= self.radius

    def is_inside_cube(self, a_cube):
        # Determine if all eight corners of the Cube are strictly inside the Sphere
        for corner in a_cube.corners():
            if not self.is_inside_point(corner):
                return False
        return True

    def does_intersect_sphere(self, other):
        return self.distance(other) <= self.radius + other.radius

    def does_intersect_cube(self, a_cube):
        # Two objects intersect if they are not strictly inside or not strictly outside each other
        return not self.is_inside_cube(a_cube) and not a_cube.is_inside_sphere(self)

    def circumscribe_cube(self):
        # Return the largest Cube object that is circumscribed by this Sphere
        # All eight corners of the Cube are on the Sphere
        return Cube(self.x, self.y, self.z, 2 * self.radius)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

class Cube(object):
    def __init__(self, x=0, y=0, z=0, side=1):
        self.x = x
        self.y = y
        self.z = z
        self.side = side

    def __str__(self):
        return f"Center: ({self.x:.1f}, {self.y:.1f}, {self.z:.1f}), Side: {self.side:.1f}"

    def area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3

    def is_inside_point(self, p):
        half_side = self.side / 2
        return (
            abs(self.x - p.x) <= half_side and
            abs(self.y - p.y) <= half_side and
            abs(self.z - p.z) <= half_side
        )

    def is_inside_sphere(self, a_sphere):
        return a_sphere.is_inside_cube(self)

    def is_inside_cube(self, other):
        half_side = self.side / 2
        return (
            abs(self.x - other.x) + half_side <= other.side / 2 and
            abs(self.y - other.y) + half_side <= other.side / 2 and
            abs(self.z - other.z) + half_side <= other.side / 2
        )

    def does_intersect_cube(self, other):
        return not self.is_inside_cube(other) and not other.is_inside_cube(self)

    def intersection_volume(self, other):
        if not self.does_intersect_cube(other):
            return 0.0

        half_side_self = self.side / 2
        half_side_other = other.side / 2

        dx = abs(self.x - other.x) - half_side_self - half_side_other
        dy = abs(self.y - other.y) - half_side_self - half_side_other
        dz = abs(self.z - other.z) - half_side_self - half_side_other

        # Intersection volume is the product of the dimensions in the positive range
        volume = max(0, dx) * max(0, dy) * max(0, dz)
        return volume

    def inscribe_sphere(self):
        # Return the largest Sphere object that is inscribed by this Cube
        # The Sphere is inside the Cube, and the faces of the Cube are tangential planes of the Sphere
        radius = self.side / 2
        return Sphere(self.x, self.y, self.z, radius)

class Cylinder(object):
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height

    def __str__(self):
        return f"Center: ({self.x:.1f}, {self.y:.1f}, {self.z:.1f}), Radius: {self.radius:.1f}, Height: {self.height:.1f}"

    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def is_inside_point(self, p):
        distance = math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        return (
            distance <= self.radius and
            p.z >= self.z - self.height / 2 and
            p.z <= self.z + self.height / 2
        )

    def is_inside_sphere(self, a_sphere):
        return a_sphere.is_inside_cylinder(self)

    def is_inside_cube(self, a_cube):
        # Determine if all eight corners of the Cube are inside the Cylinder
        for corner in a_cube.corners():
            if not self.is_inside_point(corner):
                return False
        return True

    def is_inside_cylinder(self, other):
        return (
            other.radius <= self.radius and
            other.height / 2 <= self.height / 2 and
            math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2) + other.radius <= self.radius
        )

def main():
    # Read data from standard input
    input_data = []

    # Read coordinates of Point p
    p_coords = input().split()
    p = Point(float(p_coords[0]), float(p_coords[1]), float(p_coords[2]))
    input_data.append(p)

    # Read coordinates of Point q
    q_coords = input().split()
    q = Point(float(q_coords[0]), float(q_coords[1]), float(q_coords[2]))
    input_data.append(q)

    # Read coordinates of center and radius of sphereA
    sphereA_coords = input().split()
    sphereA = Sphere(float(sphereA_coords[0]), float(sphereA_coords[1]), float(sphereA_coords[2]), float(sphereA_coords[3]))
    input_data.append(sphereA)

    # Read coordinates of center and radius of sphereB
    sphereB_coords = input().split()
    sphereB = Sphere(float(sphereB_coords[0]), float(sphereB_coords[1]), float(sphereB_coords[2]), float(sphereB_coords[3]))
    input_data.append(sphereB)

    # Read coordinates of center and side of cubeA
    cubeA_coords = input().split()
    cubeA = Cube(float(cubeA_coords[0]), float(cubeA_coords[1]), float(cubeA_coords[2]), float(cubeA_coords[3]))
    input_data.append(cubeA)

    # Read coordinates of center and side of cubeB
    cubeB_coords = input().split()
    cubeB = Cube(float(cubeB_coords[0]), float(cubeB_coords[1]), float(cubeB_coords[2]), float(cubeB_coords[3]))
    input_data.append(cubeB)

    # Read coordinates of center, radius, and height of cylA
    cylA_coords = input().split()
    cylA = Cylinder(float(cylA_coords[0]), float(cylA_coords[1]), float(cylA_coords[2]), float(cylA_coords[3]), float(cylA_coords[4]))
    input_data.append(cylA)

    # Read coordinates of center, radius, and height of cylB
    cylB_coords = input().split()
    cylB = Cylinder(float(cylB_coords[0]), float(cylB_coords[1]), float(cylB_coords[2]), float(cylB_coords[3]), float(cylB_coords[4]))
    input_data.append(cylB)

    # Print statements based on the provided conditions
    print(f"Distance of Point p from the origin {'is' if p.distance(Point()) > q.distance(Point()) else 'is not'} greater than the distance of Point q from the origin")
    print(f"Point p {'is' if sphereA.is_inside_point(p) else 'is not'} inside sphereA")
    print(f"sphereB {'is' if sphereB.is_inside_sphere(sphereA) else 'is not'} inside sphereA")
    print(f"cubeA {'is' if sphereA.is_inside_cube(cubeA) else 'is not'} inside sphereA")
    print(f"cylA {'is' if sphereA.is_inside_cylinder(cylA) else 'is not'} inside sphereA")
    print(f"sphereA {'does' if sphereA.does_intersect_sphere(sphereB) else 'does not'} intersect sphereB")
    print(f"cubeB {'does' if sphereB.does_intersect_cube(cubeB) else 'does not'} intersect sphereB")
    print(f"Volume of the largest Cube that is circumscribed by sphereA {'is' if sphereA.circumscribe_cube().volume() > cylA.volume() else 'is not'} greater than the volume of cylA")
    print(f"Point p {'is' if cubeA.is_inside_point(p) else 'is not'} inside cubeA")
    print(f"sphereA {'is' if cubeA.is_inside_sphere(sphereA) else 'is not'} inside cubeA")
    print(f"cubeB {'is' if cubeB.is_inside_cube(cubeA) else 'is not'} inside cubeA")
    print(f"cubeA {'does' if cubeA.does_intersect_cube(cubeB) else 'does not'} intersect cubeB")
    print(f"Intersection volume of cubeA and cubeB {'is' if cubeA.intersection_volume(cubeB) > sphereA.volume() else 'is not'} greater than the volume of sphereA")
    print(f"Surface area of the largest Sphere object inscribed by cubeA {'is' if cubeA.inscribe_sphere().area() > cylA.area() else 'is not'} greater than the surface area of cylA")
    print(f"Point p {'is' if cylA.is_inside_point(p) else 'is not'} inside cylA")
    print(f"sphereA {'is' if cylA.is_inside_sphere(sphereA) else 'is not'} inside cylA")
    print(f"cubeA {'is' if cylA.is_inside_cube(cubeA) else 'is not'} inside cylA")
    print(f"cylB {'is' if cylA.is_inside_cylinder(cylB) else 'is not'} inside cylA")

if __name__ == "__main__":
    main()

