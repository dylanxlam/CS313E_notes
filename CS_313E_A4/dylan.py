import math

class Point (object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def distance(self, other):
        dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
        return dist

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

class Sphere (object):
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.center = Point(x, y, z)
        self.radius = radius

    def __str__(self):
        return f"Center: {self.center}, Radius: {self.radius}"

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def is_inside_point(self, p):
        dist = self.center.distance(p)
        return dist < self.radius

    def is_inside_sphere(self, other):
        dist = self.center.distance(other.center)
        return dist + other.radius <= self.radius

    def is_inside_cube(self, a_cube):
        min_x = a_cube.center.x - a_cube.side / 2
        max_x = a_cube.center.x + a_cube.side / 2
        min_y = a_cube.center.y - a_cube.side / 2
        max_y = a_cube.center.y + a_cube.side / 2
        min_z = a_cube.center.z - a_cube.side / 2
        max_z = a_cube.center.z + a_cube.side / 2

        return (min_x >= self.center.x - self.radius and
                max_x <= self.center.x + self.radius and
                min_y >= self.center.y - self.radius and
                max_y <= self.center.y + self.radius and
                min_z >= self.center.z - self.radius and
                max_z <= self.center.z + self.radius)

    def does_intersect_sphere(self, other):
        dist = self.center.distance(other.center)
        return dist <= self.radius + other.radius

    def does_intersect_cube(self, a_cube):
        min_x = a_cube.center.x - a_cube.side / 2
        max_x = a_cube.center.x + a_cube.side / 2
        min_y = a_cube.center.y - a_cube.side / 2
        max_y = a_cube.center.y + a_cube.side / 2
        min_z = a_cube.center.z - a_cube.side / 2
        max_z = a_cube.center.z + a_cube.side / 2

        closest_x = max(min_x, min(max_x, self.center.x))
        closest_y = max(min_y, min(max_y, self.center.y))
        closest_z = max(min_z, min(max_z, self.center.z))

        dist = math.sqrt((closest_x - self.center.x) ** 2 +
                         (closest_y - self.center.y) ** 2 +
                         (closest_z - self.center.z) ** 2)

        return dist <= self.radius

    def circumscribe_cube(self):
        side = 2 * self.radius
        return Cube(self.center.x, self.center.y, self.center.z, side)

class Cube (object):
    def __init__(self, x=0, y=0, z=0, side=1):
        self.center = Point(x, y, z)
        self.side = side

    def __str__(self):
        return f"Center: {self.center}, Side: {self.side}"

    def area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3

    def is_inside_point(self, p):
        min_x = self.center.x - self.side / 2
        max_x = self.center.x + self.side / 2
        min_y = self.center.y - self.side / 2
        max_y = self.center.y + self.side / 2
        min_z = self.center.z - self.side / 2
        max_z = self.center.z + self.side / 2

        return (p.x >= min_x and p.x <= max_x and
                p.y >= min_y and p.y <= max_y and
                p.z >= min_z and p.z <= max_z)

    def is_inside_sphere(self, a_sphere):
        dist = a_sphere.center.distance(self.center)
        return dist + a_sphere.radius <= self.side / 2

    def is_inside_cube(self, other):
        min_x = other.center.x - other.side / 2
        max_x = other.center.x + other.side / 2
        min_y = other.center.y - other.side / 2
        max_y = other.center.y + other.side / 2
        min_z = other.center.z - other.side / 2
        max_z = other.center.z + other.side / 2

        min_x_inside = min_x >= self.center.x - self.side / 2
        max_x_inside = max_x <= self.center.x + self.side / 2
        min_y_inside = min_y >= self.center.y - self.side / 2
        max_y_inside = max_y <= self.center.y + self.side / 2
        min_z_inside = min_z >= self.center.z - self.side / 2
        max_z_inside = max_z <= self.center.z + self.side / 2

        return (min_x_inside and max_x_inside and
                min_y_inside and max_y_inside and
                min_z_inside and max_z_inside)

    def does_intersect_cube(self, other):
        min_x = self.center.x - self.side / 2
        max_x = self.center.x + self.side / 2
        min_y = self.center.y - self.side / 2
        max_y = self.center.y + self.side / 2
        min_z = self.center.z - self.side / 2
        max_z = self.center.z + self.side / 2

        min_x_other = other.center.x - other.side / 2
        max_x_other = other.center.x + other.side / 2
        min_y_other = other.center.y - other.side / 2
        max_y_other = other.center.y + other.side / 2
        min_z_other = other.center.z - other.side / 2
        max_z_other = other.center.z + other.side / 2

        x_overlap = (max_x >= min_x_other and min_x <= max_x_other)
        y_overlap = (max_y >= min_y_other and min_y <= max_y_other)
        z_overlap = (max_z >= min_z_other and min_z <= max_z_other)

        return x_overlap and y_overlap and z_overlap

    def intersection_volume(self, other):
        min_x = max(self.center.x - self.side / 2, other.center.x - other.side / 2)
        max_x = min(self.center.x + self.side / 2, other.center.x + other.side / 2)
        min_y = max(self.center.y - self.side / 2, other.center.y - other.side / 2)
        max_y = min(self.center.y + self.side / 2, other.center.y + other.side / 2)
        min_z = max(self.center.z - self.side / 2, other.center.z - other.side / 2)
        max_z = min(self.center.z + self.side / 2, other.center.z + other.side / 2)

        x_len = max_x - min_x
        y_len = max_y - min_y
        z_len = max_z - min_z

        if x_len <= 0 or y_len <= 0 or z_len <= 0:
            return 0.0
        else:
            return x_len * y_len * z_len

    def inscribe_sphere(self):
        radius = self.side / 2
        return Sphere(self.center.x, self.center.y, self.center.z, radius)

class Cylinder (object):
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.center = Point(x, y, z)
        self.radius = radius
        self.height = height

    def __str__(self):
        return f"Center: {self.center}, Radius: {self.radius}, Height: {self.height}"

    def area(self):
        side_area = 2 * math.pi * self.radius * self.height
        top_area = 2 * math.pi * self.radius ** 2
        return side_area + top_area

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def is_inside_point(self, p):
        min_x = self.center.x - self.radius
        max_x = self.center.x + self.radius
        min_y = self.center.y - self.radius
        max_y = self.center.y + self.radius
        min_z = self.center.z
        max_z = self.center.z + self.height

        inside_base = (p.x >= min_x and p.x <= max_x and
                       p.y >= min_y and p.y <= max_y and
                       p.z >= min_z and p.z <= max_z)

        dist = self.center.distance(p)
        return inside_base and dist <= self.radius

    def is_inside_sphere(self, a_sphere):
        min_x = self.center.x - self.radius
        max_x = self.center.x + self.radius
        min_y = self.center.y - self.radius
        max_y = self.center.y + self.radius
        min_z = self.center.z
        max_z = self.center.z + self.height

        dist = a_sphere.center.distance(self.center)

        return (min_x <= a_sphere.center.x - a_sphere.radius and
                max_x >= a_sphere.center.x + a_sphere.radius and
                min_y <= a_sphere.center.y - a_sphere.radius and
                max_y >= a_sphere.center.y + a_sphere.radius and
                min_z <= a_sphere.center.z - a_sphere.radius and
                max_z >= a_sphere.center.z + a_sphere.radius and
                dist + a_sphere.radius <= self.radius)

    def is_inside_cube(self, a_cube):
        min_x = self.center.x - self.radius
        max_x = self.center.x + self.radius
        min_y = self.center.y - self.radius
        max_y = self.center.y + self.radius
        min_z = self.center.z
        max_z = self.center.z + self.height

        min_x_inside = min_x >= a_cube.center.x - a_cube.side / 2
        max_x_inside = max_x <= a_cube.center.x + a_cube.side / 2
        min_y_inside = min_y >= a_cube.center.y - a_cube.side / 2
        max_y_inside = max_y <= a_cube.center.y + a_cube.side / 2
        min_z_inside = min_z >= a_cube.center.z - a_cube.side / 2
        max_z_inside = max_z <= a_cube.center.z + a_cube.side / 2

        return (min_x_inside and max_x_inside and
                min_y_inside and max_y_inside and
                min_z_inside and max_z_inside)

    def is_inside_cylinder(self, other):
        min_x = self.center.x - self.radius
        max_x = self.center.x + self.radius
        min_y = self.center.y - self.radius
        max_y = self.center.y + self.radius
        min_z = self.center.z
        max_z = self.center.z + self.height

        min_x_other = other.center.x - other.radius
        max_x_other = other.center.x + other.radius
        min_y_other = other.center.y - other.radius
        max_y_other = other.center.y + other.radius
        min_z_other = other.center.z
        max_z_other = other.center.z + other.height

        x_overlap = (max_x >= min_x_other and min_x <= max_x_other)
        y_overlap = (max_y >= min_y_other and min_y <= max_y_other)
        z_overlap = (max_z >= min_z_other and min_z <= max_z_other)

        return x_overlap and y_overlap and z_overlap

def main():
    # Read data from standard input
    p_coords = list(map(float, input().split()))
    q_coords = list(map(float, input().split()))
    sphere_a_coords = list(map(float, input().split()))
    sphere_b_coords = list(map(float, input().split()))
    cube_a_coords = list(map(float, input().split()))
    cube_b_coords = list(map(float, input().split()))
    cyl_a_coords = list(map(float, input().split()))
    cyl_b_coords = list(map(float, input().split()))

    # Create objects
    p = Point(*p_coords)
    q = Point(*q_coords)
    sphere_a = Sphere(*sphere_a_coords)
    sphere_b = Sphere(*sphere_b_coords)
    cube_a = Cube(*cube_a_coords)
    cube_b = Cube(*cube_b_coords)
    cyl_a = Cylinder(*cyl_a_coords)
    cyl_b = Cylinder(*cyl_b_coords)

    # Perform the required comparisons and calculations
    distance_p_q = "is" if p.distance(Point(0, 0, 0)) > q.distance(Point(0, 0, 0)) else "is not"
    point_p_inside_sphere_a = "is" if sphere_a.is_inside_point(p) else "is not"
    sphere_b_inside_sphere_a = "is" if sphere_a.is_inside_sphere(sphere_b) else "is not"
    cube_a_inside_sphere_a = "is" if sphere_a.is_inside_cube(cube_a) else "is not"
    sphere_a_intersects_sphere_b = "does" if sphere_a.does_intersect_sphere(sphere_b) else "does not"
    cube_b_intersects_sphere_b = "does" if cube_b.does_intersect_sphere(sphere_b) else "does not"
    circumscribe_cube_volume = "is" if sphere_a.circumscribe_cube().volume() > cyl_a.volume() else "is not"
    point_p_inside_cube_a = "is" if cube_a.is_inside_point(p) else "is not"
    sphere_a_inside_cube_a = "is" if cube_a.is_inside_sphere(sphere_a) else "is not"
    cube_b_inside_cube_a = "is" if cube_a.is_inside_cube(cube_b) else "is not"
    cube_a_intersects_cube_b = "does" if cube_a.does_intersect_cube(cube_b) else "does not"
    intersection_volume = "is" if cube_a.intersection_volume(cube_b) > sphere_a.volume() else "is not"
    inscribe_sphere_surface_area = "is" if cube_a.inscribe_sphere().area() > cyl_a.area() else "is not"
    point_p_inside_cyl_a = "is" if cyl_a.is_inside_point(p) else "is not"
    sphere_a_inside_cyl_a = "is" if cyl_a.is_inside_sphere(sphere_a) else "is not"
    cube_a_inside_cyl_a = "is" if cyl_a.is_inside_cube(cube_a) else "is not"
    cyl_b_inside_cyl_a = "is" if cyl_a.is_inside_cylinder(cyl_b) else "is not"

    # Print the results
    print(f"Distance of Point p from the origin {distance_p_q} greater than the distance of Point q from the origin")
    print(f"Point p {point_p_inside_sphere_a} inside sphereA")
    print(f"sphereB {sphere_b_inside_sphere_a} inside sphereA")
    print(f"cubeA {cube_a_inside_sphere_a} inside sphereA")
    print(f"cylA {cyl_a_inside_sphere_a} inside sphereA")
    print(f"sphereA {sphere_a_intersects_sphere_b} intersect sphereB")
    print(f"cubeB {cube_b_intersects_sphere_b} intersect sphereB")
    print(f"Volume of the largest Cube that is circumscribed by sphereA {circumscribe_cube_volume} greater than the volume of cylA")
    print(f"Point p {point_p_inside_cube_a} inside cubeA")
    print(f"sphereA {sphere_a_inside_cube_a} inside cubeA")
    print(f"cubeB {cube_b_inside_cube_a} inside cubeA")
    print(f"cubeA {cube_a_intersects_cube_b} intersect cubeB")
    print(f"Intersection volume of cubeA and cubeB {intersection_volume} greater than the volume of sphereA")
    print(f"Surface area of the largest Sphere object inscribed by cubeA {inscribe_sphere_surface_area} greater than the surface area of cylA")
    print(f"Point p {point_p_inside_cyl_a} inside cylA")
    print(f"sphereA {sphere_a_inside_cyl_a} inside cylA")
    print(f"cubeA {cube_a_inside_cyl_a} inside cylA")
    print(f"cylB {cyl_b_inside_cyl_a} inside cylA")

if __name__ == "__main__":
    main()
      
