#  File: OfficeSpace.py

#  Description:

#  Student Name: Dylan Lam

#  Student UT EID: DXL85

#  Partner Name: Alexander Romero-Barrionuevo

#  Student's UT EID: ANR3784    

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created:

#  Date Last Modified:


# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area(rect):
    return (rect[2] - rect[0]) * (rect[3] - rect[1])

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested space in the office
def contested_space(bldg):
    contested = 0
    for row in bldg:
        for cell in row:
            if cell > 1:
                contested += 1
    return contested

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested space in the office that the employee gets
def uncontested_space(bldg, rect):
    area_requested = area(rect)
    uncontested_area = 0
    for i in range(rect[0], rect[2]):
        for j in range(rect[1], rect[3]):
            if bldg[j][i] == 1:
                uncontested_area += 1
    return uncontested_area

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space(office, cubicles):
    w = office[2]
    h = office[3]
    bldg = [[0] * w for _ in range(h)]

    for i, (employee, rect) in enumerate(cubicles):
        for x in range(rect[0], rect[2]):
            for y in range(rect[1], rect[3]):
                if bldg[y][x] == 0:
                    bldg[y][x] = i + 1
                else:
                    # Mark as contested with the employee index
                    bldg[y][x] = -1

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
        total_area = (x2 - x1) * (y2 - y1)
        cubicles.append((employee, (x1, y1, x2, y2)))

    # Calculate contested space
    bldg = request_space((0, 0, w, h), cubicles)
    contested = contested_space(bldg)

    # Calculate and print results
    total_space = w * h
    unallocated = sum(row.count(0) for row in bldg)
    print(f"Total {total_space}")
    print(f"Unallocated {unallocated}")
    print(f"Contested {contested}")

    for employee, rect in cubicles:
        area_allocated = uncontested_space(bldg, rect)
        print(f"{employee} {area_allocated}")

if __name__ == "__main__":
    main()
