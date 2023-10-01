
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
def area(rect):
    return (rect[2] - rect[0]) * (rect[3] - rect[1])

def overlap(rect1, rect2):
    x1 = max(rect1[0], rect2[0])
    y1 = max(rect1[1], rect2[1])
    x2 = min(rect1[2], rect2[2])
    y2 = min(rect1[3], rect2[3])

    if x1 < x2 and y1 < y2:
        return (x1, y1, x2, y2)
    else:
        return (0, 0, 0, 0)

def unallocated_space(bldg):
    unallocated = 0
    for row in bldg:
        unallocated += row.count(0)
    return unallocated

def contested_space(bldg):
    contested = 0
    for i in range(len(bldg)):
        for j in range(len(bldg[0])):
            if bldg[i][j] < 0:
                contested += 1
    return contested

def uncontested_space(bldg, rect):
    x1, y1, x2, y2 = rect
    area_requested = area(rect)
    overlapping_area = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if bldg[j][i] < 0:
                overlapping_area += 1
    return area_requested - overlapping_area




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
