#  File: OfficeSpace.py

#  Description: This program efficiently allocates office cubicles 
#  to employees based on their placement requests. It calculates key 
#  metrics such as total office space, unallocated space, contested space, 
#  and individual allocations for each employee.

#  Student Name: Alexander Romero

#  Student UT EID: ANR3784

#  Partner Name: Dylan Lam

#  Partner UT EID: DXL85

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created: 9/30/2023

#  Date Last Modified: 9/30/2023


# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area(rect):
    return (rect[2] - rect[0]) * (rect[3] - rect[1])

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap(rect1, rect2):
    x1 = max(rect1[0], rect2[0])
    y1 = max(rect1[1], rect2[1])
    x2 = min(rect1[2], rect2[2])
    y2 = min(rect1[3], rect2[3])

    if x1 < x2 and y1 < y2:
        return (x1, y1, x2, y2)
    else:
        return (0, 0, 0, 0)
    

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space(bldg):
    contested = 0
    for row in bldg:
        for cell in row:
            if cell > 1:
                contested += 1
    return contested
    

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space(bldg):
    unallocated = 0
    for row in bldg:
        unallocated += row.count(0)
    return unallocated


# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the contested 
#         space in the office for the specified employee
def contested_area(bldg, rect):
    # Get respective coordinates and establish variable of area
    x1, y1, x2, y2 = rect
    contested = 0

    # Check through the building and see how many spaces are contested
    for x in range(x1, x2):
        for y in range(y1, y2):
            if bldg[y][x] > 1:
                contested += 1

    return contested

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space(bldg, rect):
    # Get respective coordinates and establish variable of area
    uncontested = 0
    x1, y1, x2, y2 = rect

     # Check through the building and see how many spaces are uncontested
    for i in range(y1, y2):
        for j in range(x1, x2):
            if bldg[i][j] == 1:
                uncontested += 1

    return uncontested


# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space(office, cubicles):
    # Find width and height of office, create an empty 2D list by dimensions
    w = office[2]
    h = office[3]
    bldg = [[0] * w for _ in range(h)]

    # Iterate through the 2D list and populate cubicles by number of instances of employees
    for i, (employee, rect) in enumerate(cubicles):
        for x in range(rect[0], rect[2]):
            for y in range(rect[1], rect[3]):
                bldg[y][x] += 1

    return bldg

def main():
    # Read office space size
    w, h = map(int, input().split())

    # Read number of employees
    n = int(input())

    # Create office building as a 2D array initialized with 0
    office = [[0] * w for _ in range(h)]

    # Initialize dictionaries to store the total and allocated areas for each employee
    total_areas = {}
    allocated_areas = {}

    # Read employee requests and process them
    cubicles = []
    for _ in range(n):
        employee, x1, y1, x2, y2 = input().split()
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
        cubicles.append((employee, (x1, y1, x2, y2)))

    # Create office building and allocate spaces
    bldg = request_space((0, 0, w, h), cubicles)

    # Calculate and print results
    total_space = w * h
    unallocated = unallocated_space(bldg)
    contested = contested_space(bldg)
    print(f"Total {total_space}")
    print(f"Unallocated {unallocated}")
    print(f"Contested {contested}")

    for employee, rect in cubicles:
        area_allocated = uncontested_space(bldg, rect)
        print(f"{employee} {area_allocated}")

if __name__ == "__main__":
    main()