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

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__ (self):
        return f"({float(self.x)}, {float(self.y)}, {float(self.z)})"
    
    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance (self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
    
    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__ (self, other):
        tolerance = 1e-6
        return (
        abs(self.x - other.x) < tolerance and
        abs(self.y - other.y) < tolerance and
        abs(self.z - other.z) < tolerance
        )

class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
        return f"Center: ({float(self.x)}, {float(self.y)}, {float(self.z)}), Radius: {float(self.radius)}"
    
    # compute surface area of Sphere
    # returns a floating point number
    def area (self):
        return 4 * math.pi * self.radius**2
    
    # compute volume of a Sphere
    # returns a floating point number
    def volume (self):
        return (4/3) * math.pi * self.radius**3
    
    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point (self, p):
        distance_squared = (p.x - self.x)**2 + (p.y - self.y)**2 + (p.z - self.z)**2
        return distance_squared < self.radius**2
    
    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, other):
        distance_between_centers = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
        return distance_between_centers + other.radius < self.radius
    
    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly 
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        for corner in a_cube.corners():
            if not self.is_inside_point(corner):
                return False
        return True
    
    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere (self, other):
        distance_between_centers = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
        return distance_between_centers < self.radius + other.radius

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, a_cube):
        # Check if any of the Cube's corners is inside the Sphere or vice versa
        for corner in a_cube.corners():
            if self.is_inside_point(corner) or a_cube.is_inside_point(Point(self.x, self.y, self.z)):
                return True
        
        # Check if any Sphere's center is inside the Cube
        return a_cube.is_inside_point(Point(self.x, self.y, self.z))
    
    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):
        side_length = 2 * self.radius
        return Cube(self.x, self.y, self.z, side_length)



class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.x = x
        self.y = y
        self.z = z
        self.side = side

    # string representation of a Cube of the form: 
    # Center: (x, y, z), Side: value
    def __str__ (self):
        return f"Center: ({float(self.x)}, {float(self.y)}, {float(self.z)}), Side: {float(self.side)}"

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self):
        return 6 * self.side ** 2

    # compute volume of a Cube
    # returns a floating point number
    def volume (self):
        return self.side ** 3

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, p):
        half_side = self.side / 2
        return (
            abs(p.x - self.x) <= half_side and
            abs(p.y - self.y) <= half_side and
            abs(p.z - self.z) <= half_side
        )

    # determine if a Sphere is strictly inside this Cube 
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        half_side = self.side / 2
        return (
            a_sphere.x - a_sphere.radius >= self.x - half_side and
            a_sphere.x + a_sphere.radius <= self.x + half_side and
            a_sphere.y - a_sphere.radius >= self.y - half_side and
            a_sphere.y + a_sphere.radius <= self.y + half_side and
            a_sphere.z - a_sphere.radius >= self.z - half_side and
            a_sphere.z + a_sphere.radius <= self.z + half_side
        )

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        self_corners = self.corners()
        for corner in self_corners:
            if not other.is_inside_point(corner):
                return False
        return True

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, other):
        self_corners = self.corners()
        for corner in self_corners:
            if other.is_inside_point(corner):
                return True
        return False

    # determine the volume of intersection if this Cube 
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        if not self.does_intersect_cube(other):
            return 0

        self_corners = self.corners()
        intersection_points = [point for point in self_corners if other.is_inside_point(point)]
        return len(intersection_points) * self.side ** 3 / 8

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        radius = self.side / 2
        return Sphere(self.x, self.y, self.z, radius)

    # Calculate and return the corners of the cube
    # returns a list of Point objects representing corners
    def corners(self):
        half_side = self.side / 2
        corners = [
            Point(self.x - half_side, self.y - half_side, self.z - half_side),
            Point(self.x + half_side, self.y - half_side, self.z - half_side),
            Point(self.x - half_side, self.y + half_side, self.z - half_side),
            Point(self.x - half_side, self.y - half_side, self.z + half_side),
            Point(self.x + half_side, self.y + half_side, self.z - half_side),
            Point(self.x + half_side, self.y - half_side, self.z + half_side),
            Point(self.x - half_side, self.y + half_side, self.z + half_side),
            Point(self.x + half_side, self.y + half_side, self.z + half_side)
        ]
        return corners



class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius, and height. The main axis of the Cylinder is along the
    # z-axis, and height is measured along this axis.
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height

    # Returns a string representation of a Cylinder of the form: 
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):
        return f"Center: ({self.x}, {self.y}, {self.z}), Radius: {self.radius}, Height: {self.height}"

    # Compute surface area of Cylinder
    # Returns a floating-point number
    def area (self):
        return 2 * math.pi * self.radius * self.radius + 2 * math.pi * self.radius * self.height

    # Compute volume of a Cylinder
    # Returns a floating-point number
    def volume (self):
        return math.pi * self.radius * self.radius * self.height

    # Determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # Returns a Boolean
    def is_inside_point (self, p):
        distance = math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        return (
            distance <= self.radius and
            p.z >= self.z and
            p.z <= self.z + self.height
        )

    # Determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # Returns a Boolean
    def is_inside_sphere (self, a_sphere):
        distance = math.sqrt((self.x - a_sphere.x) ** 2 + (self.y - a_sphere.y) ** 2)
        return (
            distance + a_sphere.radius <= self.radius and
            a_sphere.z >= self.z and
            a_sphere.z <= self.z + self.height
        )

    # Determine if a Cube is strictly inside this Cylinder
    # Determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # Returns a Boolean
    def is_inside_cube (self, a_cube):
        corners = a_cube.corners()
        for corner in corners:
            if not self.is_inside_point(corner):
                return False
        return True

    # Determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # Returns a Boolean
    def is_inside_cylinder (self, other):
        return (
            other.radius <= self.radius and
            other.height <= self.height and
            self.is_inside_point(Point(other.x, other.y, other.z))
        )



def main():
    # Read input data from standard input
    input_data = sys.stdin.readlines()

    # Initialize a list to store extracted numbers
    numbers = []

    # Iterate through each line of input
    for line in input_data:
        # Split the line by spaces to separate numbers and other characters
        parts = line.split()

        # Extract and convert the numbers to floats
        for part in parts:
            try:
                num = float(part)
                numbers.append(num)
            except ValueError:
                # If conversion to float fails, ignore the part (possibly a comment)
                pass
    
    # read the coordinates of the first Point p and create a Point object 
    point_p = Point(numbers[0], numbers[1], numbers[2])

    # # read the coordinates of the second Point q and create a Point object
    point_q = Point(numbers[3], numbers[4], numbers[5])

    # read the coordinates of the center and radius of sphereA and create a Sphere object
    sphereA = Sphere(numbers[6], numbers[7], numbers[8], numbers[9])

    # read the coordinates of the center and radius of sphereB and create a Sphere object
    sphereB = Sphere(numbers[10], numbers[11], numbers[12], numbers[13])

    # read the coordinates of the center and side of cubeA and create a Cube object 
    cubeA = Cube(numbers[14], numbers[15], numbers[16], numbers[17])

    # read the coordinates of the center and side of cubeB and create a Cube object 
    cubeB = Cube(numbers[18], numbers[19], numbers[20], numbers[21])

    # read the coordinates of the center, radius and height of cylA and create a Cylinder object 
    cylA = Cylinder(numbers[22], numbers[23], numbers[24], numbers[25], numbers[26])

    # read the coordinates of the center, radius and height of cylB and create a Cylinder object
    cylB = Cylinder(numbers[27], numbers[28], numbers[29], numbers[30], numbers[31])
    
    # print if the distance of p from the origin (is / is not) greater than the distance of q from the origin
    distance_p = point_p.distance(Point(0, 0, 0))
    distance_q = point_q.distance(Point(0, 0, 0))
    print(f"Distance of Point p from the origin {'is' if distance_p > distance_q else 'is not'} greater than the distance of Point q from the origin")

    # print if Point p (is / is not) inside sphereA
    print(f"Point p {'is' if sphereA.is_inside_point(point_p) else 'is not'} inside sphereA")

    # print if sphereB (is / is not) inside sphereA
    print(f"sphereB {'is' if sphereA.is_inside_sphere(sphereB) else 'is not'} inside sphereA")

    # print if cubeA (is / is not) inside sphereA
    print(f"cubeA {'is' if sphereA.is_inside_cube(cubeA) else 'is not'} inside sphereA")

    # print if sphereA (does / does not) intersect sphereB
    print(f"sphereA {'does' if sphereA.does_intersect_sphere(sphereB) else 'does not'} intersect sphereB")

    # print if cubeB (does / does not) intersect sphereB
    print(f"cubeB {'does' if sphereB.does_intersect_cube(cubeB) else 'does not'} intersect sphereB")

    # print if the volume of the largest Cube that is circumscribed by sphereA (is / is not) greater than the volume of cylA
    circumscribed_cube_volume = sphereA.circumscribe_cube().volume()
    cylA_volume = cylA.volume()
    print(f"Volume of the largest Cube that is circumscribed by sphereA {'is' if circumscribed_cube_volume > cylA_volume else 'is not'} greater than the volume of cylA")

    # print if Point p (is / is not) inside cubeA
    print(f"Point p {'is' if cubeA.is_inside_point(point_p) else 'is not'} inside cubeA")

    # print if sphereA (is / is not) inside cubeA
    print(f"sphereA {'is' if cubeA.is_inside_sphere(sphereA) else 'is not'} inside cubeA")

    # print if cubeB (is / is not) inside cubeA
    print(f"cubeB {'is' if cubeA.is_inside_cube(cubeB) else 'is not'} inside cubeA")

    # print if cubeA (does / does not) intersect cubeB
    print(f"cubeA {'does' if cubeA.does_intersect_cube(cubeB) else 'does not'} intersect cubeB")

    # print if the intersection volume of cubeA and cubeB (is / is not) greater than the volume of sphereA
    intersection_vol = cubeA.intersection_volume(cubeB)
    sphereA_vol = sphereA.volume()
    print(f"Intersection volume of cubeA and cubeB {'is' if intersection_vol > sphereA_vol else 'is not'} greater than the volume of sphereA")

    # print if the surface area of the largest Sphere object inscribed by cubeA (is / is not) greater than the surface area of cylA
    inscribed_sphere_area = cubeA.inscribe_sphere().area()
    cylA_area = cylA.area()
    print(f"Surface area of the largest Sphere inscribed by cubeA {'is' if inscribed_sphere_area > cylA_area else 'is not'} greater than the surface area of cylA")

    # print if Point p (is / is not) inside cylA
    print(f"Point p {'is' if cylA.is_inside_point(point_p) else 'is not'} inside cylA")

    # print if sphereA (is / is not) inside cylA
    print(f"sphereA {'is' if cylA.is_inside_sphere(sphereA) else 'is not'} inside cylA")

    # print if cubeA (is / is not) inside cylA
    print(f"cubeA {'is' if cylA.is_inside_cube(cubeA) else 'is not'} inside cylA")

    # print if cylB (is / is not) inside cylA
    print(f"cylB {'is' if cylA.is_inside_cylinder(cylB) else 'is not'} inside cylA")
        
if __name__ == "__main__":
  main()