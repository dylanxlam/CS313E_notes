from __future__ import division
import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = x
      self.y = y
      self.z = z
  # create a string representation of a Point (x, y, z)
  def __str__ (self):
      return str('(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')')
  # get distance to another Point object
  def distance (self, other):
      x2 = (self.x - other.x) * (self.x - other.x)
      y2 = (self.y - other.y) * (self.y - other.y)
      z2 = (self.z - other.z) * (self.z - other.z)
      return ((x2 + y2 + z2) ** 0.5)
  # test for equality between two points
  def __eq__ (self, other):
      return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
      self.center = Point(x,y,z)
      self.radius = radius
  # string representation of a Sphere: Center: (x, y, z), Radius: value
  def __str__ (self):
      return str('Center: '+ '(' + str(self.center.x) + ','+ str(self.center.y)+ ',' + str(self.center.z)+'), Radius: ' +str(self.radius))
  # compute surface area of Sphere
  def area (self):
      return 4 * math.pi * ((self.radius) ** 2)
  # compute volume of a Sphere
  def volume (self):
      return (4/3) * math.pi * ((self.radius) ** 3)
   # determines if a Point is strictly inside the Sphere
  def is_inside_point (self, p):
    dist = p.distance (self.center)
    if (dist < self.radius):
        return 'is'
    return 'is not'
  # determine if another Sphere is strictly inside this Sphere
  def is_inside_sphere (self, other):
    dist = self.center.distance (other.center)
    if (self.radius > (dist + other.radius)):
        return 'is'
    return 'is not'
  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are inside
  # the Sphere
  def is_inside_cube (self, a_cube):
    dist = self.center.distance(a_cube.center)
    if dist + math.sqrt(2)*a_cube.side*.5 > self.radius:
        return 'is not'
    else:
        return 'is'
  #  (optional) determine if a Cylinder is strictly inside this Sphere
  def is_inside_cyl (self, a_cyl):
    if abs(self.radius) > abs(self.center.x - a_cyl.center.x - a_cyl.radius) and abs(self.radius) > abs(self.center.y - a_cyl.center.y - a_cyl.radius) and abs(self.radius) > abs(self.center.z - a_cyl.center.z - .5*a_cyl.height):
        return 'is'
    return 'is not'
  # determine if another Sphere intersects this Sphere
  # there is a non-zero volume of intersection
  def does_intersect (self, other):
    dist = self.center.distance (other.center)
    if (dist < (self.radius + other.radius)):
        return 'does'
    return 'does not'
  # there is at least one corner of the Cube in
  # the Sphere
  def does_intersect_cube (self, a_cube):
      if ((math.sqrt(2)*a_cube.side*.5) + self.radius)  > self.center.distance(a_cube.center):
          return 'does'
      return 'does not'
  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  def circumscribe_cube (self):
      CircumscribedCube = Cube(self.center.x,self.center.y,self.center.z,(self.radius/(math.sqrt(3)*.5)))
      return CircumscribedCube
class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
      self.center = Point (x,y,z)
      self.side = side
  # string representation of a Cube: Center: (x, y, z), Side: value
  def __str__ (self):
      return str('Center: (' + str(self.center.x)+', ' +str(self.center.y) +', ' +str(self.center.z)+ '), Side: ' +str(self.side))
  # compute surface area of Cube
  def area (self):
      return 6*self.side*self.side
  # compute volume of a Cube
  def volume (self):
      return self.side ** 3
  # determines if a Point is strictly inside this Cube
  def is_inside_point (self, p):
      if p.distance(self.center) < (self.side*.5):
          return 'is'
      return 'is not'
  # determine if a Sphere is strictly inside this Cube or
  # determine if the smallest cube that contains the Sphere
  # is within the Cube
  def is_inside_sphere (self, a_sphere):
    dist = self.center.distance (a_sphere.center)
    if (self.side*.5 > (dist + (a_sphere.radius*.5))):
        return 'is'
    return 'is not'
  # determine if another Cube is strictly inside this Cube
  def is_inside_cube (self, other):
      dist = self.center.distance (other.center)
      if (self.side*.5 > (dist + (other.side*.5))):
          return 'is'
      return 'is not'
  # determine if a Cylinder is strictly inside this Cube
  def is_inside_cylinder (self, a_cyl):
      if abs(self.center.x - a_cyl.center.x - a_cyl.radius) >= self.side*.5:
          return 'is not'
      if abs(self.center.y - a_cyl.center.y - a_cyl.radius) >= self.side*.5:
          return 'is not'
      if abs(self.center.z - a_cyl.center.z - a_cyl.height*.5) >= self.side*.5:
          return 'is not'
      return 'is'
  # determine if another Cube intersects this Cube
  # there is a non-zero volume of intersection
  # there is at least one vertex of the other Cube
  # in this Cube
  def does_intersect_cube (self, other):
      dist = self.center.distance(other.center)
      if dist < (self.side*.5+other.side*.5):
          return 'does'
      return 'does not'
  # determine the volume of intersection if this Cube
  # intersects with another Cube
  def intersection_volume (self, other):
      p1 = abs(((self.side*.5 + other.side*.5) - abs(self.center.y - other.center.y)) * ((self.side*.5 + other.side*.5) - abs(self.center.x - other.center.x)))
      p2 = (p1 * ((self.side*.5 + other.side*.5) - abs(self.center.z - other.center.z)))
      return p2
  # return the largest Sphere object that is inscribed
  # by this Cube
  def inscribe_sphere (self):
      InscribedSphere = Sphere(self.center.x,self.center.y,self.center.z,(self.side*.5))
      return InscribedSphere
class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.center = Point (x,y,z)
      self.radius = radius
      self.height = height
  # string representation of a Cylinder: Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      return str('Center: (' + str(self.center.x)+', ' +str(self.center.y)+', ' +str(self.center.z)+ '), Radius: ' +str(self.radius) + ', Height: ' + str(self.height))
  # compute surface area of Cylinder
  def area (self):
      return 2 * math.pi*self.radius*self.height + 2*math.pi*self.radius*self.radius
  # compute volume of a Cylinder
  def volume (self):
      return math.pi*self.radius*self.radius*self.height
  # determine if a Point is strictly inside this Cylinder
  def is_inside_point (self, p):
      if abs(p.x - self.center.x) >= self.radius:
          return 'is not'
      if abs(p.y - self.center.y) >= self.radius:
          return 'is not'
      if abs(p.z - self.center.z) >= self.height*.5:
          return 'is not'
      return 'is'
  # determine if a Sphere is strictly inside this Cylinder
  def is_inside_sphere (self, a_sphere):
      if abs(self.center.x - a_sphere.center.x - a_sphere.radius) >= self.radius:
          return 'is not'
      if abs((self.center.y - a_sphere.center.y - a_sphere.radius)) >= self.radius:
          return 'is not'
      if abs(self.center.z - a_sphere.center.z - a_sphere.radius) >= self.height*.5:
          return 'is not'
      return 'is'
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are in
  # the Cylinder
  def is_inside_cube (self, a_cube):
      if abs(self.center.x - a_cube.center.x - a_cube.side*.5) >= self.radius:
          return 'is not'
      if abs((self.center.y - a_cube.center.y - a_cube.side*.5)) >= self.radius:
          return 'is not'
      if abs(self.center.z - a_cube.center.z - a_cube.side*.5) >= self.height*.5:
          return 'is not'
      return 'is'
  # determine if another Cylinder is strictly inside this Cylinder
  def is_inside_cylinder (self, other):
      if abs(self.center.x - other.center.x - other.radius) >= self.radius:
          return 'is not'
      if abs((self.center.y - other.center.y - other.radius)) >= self.radius:
          return 'is not'
      if abs(self.center.z - other.center.z - other.height*.5) >= self.height*.5:
          return 'is not'
      return 'is'
  # (optional) determine if another Cylinder intersects this Cylinder
  # there is a non-zero volume of intersection
  def does_intersect_cylinder (self, other):
      x2 = (self.center.x - other.center.x) * (self.center.x - other.center.x)
      y2 = (self.center.y - other.center.y) * (self.center.y - other.center.y)
      if((x2 + y2) ** 0.5) < (self.radius + other.radius):
          if abs(self.center.z - other.center.z) <= (self.height*.5+other.height*.5):
              return 'does'
      return 'does not'
def main():
  with open('geometry.txt') as GeomFile: #We need to read from the nim.txt file. No error handling.
      Inputtext = GeomFile.read().splitlines()
  # read the coordinates of the first Point p
      pCenter = Inputtext[0].split()
      pCenter = map(float, pCenter)
  # create a Point object and print its coordinates
      p = Point(pCenter[0], pCenter[1], pCenter[2])
      print('Point p: ' + str(p))
  # read the coordinates of the second Point q
      qCenter = Inputtext[1].split()
      qCenter = map(float, qCenter)
  # create a Point object and print its coordinates
      q = Point(qCenter[0], qCenter[1], qCenter[2])
      print('Point q: ' + str(q))
  # read the coordinates of the center and radius of sphereA
      aCenter = Inputtext[2].split()
      aCenter = map(float, aCenter)
  # create a Sphere object and print it
      sphereA = Sphere(aCenter[0], aCenter[1], aCenter[2], aCenter[3])
      print('sphereA: ' + str(sphereA))
  # read the coordinates of the center and radius of sphereB
      bCenter = Inputtext[3].split()
      bCenter = map(float, bCenter)
  # create a Sphere object and print it
      sphereB = Sphere(bCenter[0], bCenter[1], bCenter[2], bCenter[3])
      print('sphereB: ' + str(sphereB))
  # read the coordinates of the center and side of cubeA
      A1Center = Inputtext[4].split()
      A1Center = map(float, A1Center)
  # create a Cube object and print it
      cubeA = Cube(A1Center[0], A1Center[1], A1Center[2], A1Center[3])
      print('cubeA: ' + str(cubeA))
  # read the coordinates of the center and side of cubeB
      B1Center = Inputtext[5].split()
      B1Center = map(float, B1Center)
  # create a Cube object and print it
      cubeB = Cube(B1Center[0], B1Center[1], B1Center[2], B1Center[3])
      print('cubeB: ' + str(cubeB))
  # read the coordinates of the center, radius and height of cylA
      CCenter = Inputtext[6].split()
      CCenter = map(float, CCenter)
  # create a Cylinder object and print it
      CylinderA = Cylinder(CCenter[0], CCenter[1], CCenter[2], CCenter[3], CCenter[4])
      print('cylA: ' + str(CylinderA))
  # read the coordinates of the center, radius and height of cylB
      C2Center = Inputtext[7].split()
      C2Center = map(float, C2Center)
  # create a Cylinder object and print it
      CylinderB = Cylinder(C2Center[0], C2Center[1], C2Center[2], C2Center[3], C2Center[4])
      print('cylB: ' + str(CylinderB))
      print('\n')
  # close file geometry.txt
  #done
  # print distance between p and q
  dist = p.distance(q)
  print('Distance between p and q: ' + str(dist))
  print('\n')
  # print area of sphereA
  area = sphereA.area()
  print('Area of sphereA: ' + str(area))
  # print volume of sphereA
  volume = sphereA.volume()
  print('Volume of sphereA: ' + str(volume))
  # print if Point p is inside sphereA
  print('Point p '+sphereA.is_inside_point(p)+' inside sphereA')
  # print if sphereB is inside sphereA
  print('sphereB '+sphereA.is_inside_sphere(sphereB)+' inside sphereA')
  # print if cubeA is inside sphereA
  print('cubeA '+sphereA.is_inside_cube(cubeA)+' inside sphereA')
  #  (optional) print if cylA is inside sphereA
  print('cylA '+sphereA.is_inside_cyl(CylinderA)+' inside sphereA')
  # print if sphereA intersects with sphereB
  print('sphereA '+sphereA.does_intersect(sphereB)+' intersect sphereB')
  # print if cubeB intersects with sphereB
  print('cubeB '+sphereB.does_intersect_cube(cubeB)+' intersect sphereB')
  # print the largest Cube that is circumscribed by sphereA
  print('Largest Cube circumscribed by sphereA: ' + str(sphereA.circumscribe_cube()))
  # print area of cubeA
  print('\n')
  print('Area of cubeA: ' + str(cubeA.area()))
  # print volume of cubeA
  print('Volume of cubeA: ' + str(cubeA.volume()))
  # print if Point p is inside cubeA
  print('Point p '+cubeA.is_inside_point(p)+' inside cubeA')
  # print if sphereA is inside cubeA
  print('sphereA '+cubeA.is_inside_sphere(sphereA)+' inside cubeA')
  # print if cubeB is inside cubeA
  print('cubeB '+cubeA.is_inside_cube(cubeB)+' inside cubeA')
  # print if cylA is inside cubeA
  print('cylA '+cubeA.is_inside_cylinder(CylinderA)+' inside cubeA')
  # print if cubeA intersects with cubeB
  print('cubeA ' +cubeB.does_intersect_cube(cubeA)+' intersect cubeB')
  # print the intersection volume of cubeA and cubeB
  print('Intersection volume of cubeA and cubeB: ' +str(cubeB.intersection_volume(cubeA)))
  # print the largest Sphere object inscribed by cubeA
  print('Largest Sphere inscribed by cubeA: ' + str(cubeA.inscribe_sphere()))
  print('\n')
  # print area of cylA
  print('Area of cylA: ' + str(CylinderA.area()))
  # print volume of cylA
  print('Volume of cylA: ' + str(CylinderA.volume()))
  # print if Point p is inside cylA
  print('Point p '+CylinderA.is_inside_point(p)+' inside cylA')
  # print if sphereA is inside cylA
  print('sphereA '+CylinderA.is_inside_sphere(sphereA)+' inside cylA')
  # print if cubeA is inside cylA
  print('cubeA '+CylinderA.is_inside_cube(cubeA)+' inside cylA')
  # print if cylB is inside cylA
  print('cylB '+CylinderA.is_inside_cylinder(CylinderB)+' inside cylA')
  # (optional) print if cylB intersects with cylA
  print('cylA '+CylinderA.does_intersect_cylinder(CylinderB)+' intersect with cylB')
main()