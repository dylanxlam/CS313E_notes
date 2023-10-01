
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
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space(bldg):
    unallocated = 0
    for row in bldg:
        unallocated += row.count(0)
    return unallocated

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space(bldg):
    contested = 0
    for row in bldg:
        for cell in row:
            if cell == -1:
                contested += 1
    return contested

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
#        test_case is a string indicating the test case type
# Output: an integer denoting the area based on the test case
def calculate_area(bldg, rect, test_case):
    area_requested = area(rect)
    overlapping_area = 0

    if test_case == "uncontested":
        for i in range(rect[0], rect[2]):
            for j in range(rect[1], rect[3]):
                if bldg[j][i] == -1:
                    overlapping_area += 1
        return area_requested - overlapping_area

    elif test_case == "contested":
        for i in range(rect[0], rect[2]):
            for j in range(rect[1], rect[3]):
                if bldg[j][i] < 0:
                    overlapping_area += 1
        return overlapping_area

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
                    # Mark as contested if already assigned
                    bldg[y][x] = -1

    return bldg

def main():
    # Read office space size
    w, h = map(int, input().split())

    # Read number of employees
    n = int(input())

    # Create office building as a 2D array initialized with 0
    office = [[0] * w for _ in range(h)]

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
        area_allocated = calculate_area(bldg, rect, "uncontested")
        print(f"{employee} {area_allocated}")

        area_contested = calculate_area(bldg, rect, "contested")
        print(f"{employee} {area_contested}")

if __name__ == "__main__":
    main()
