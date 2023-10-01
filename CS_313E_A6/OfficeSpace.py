
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
            if bldg[i][j] > 1:
                contested += 1
    return contested

def uncontested_space(bldg, rect):
    x1, y1, x2, y2 = rect
    overlapping_area = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if bldg[j][i] > 1:
                overlapping_area += 1
    return area(rect) - overlapping_area





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
    # Read the office space dimensions
    w, h = map(int, input().split())
    
    # Create a 2D list to represent the office space
    office_space = [[0] * w for _ in range(h)]
    
    # Read the number of employees
    n = int(input())
    
    # Create a dictionary to store the requested cubicles for each employee
    cubicles = {}
    
    for _ in range(n):
        line = input().split()
        employee = line[0]
        x1, y1, x2, y2 = map(int, line[1:])
        cubicles[employee] = (x1, y1, x2, y2)
    
    # Initialize variables to keep track of the office space statistics
    total_space = w * h
    unallocated_space = total_space
    contested_space = 0
    
    # Process each employee's cubicle request
    for employee, cubicle in cubicles.items():
        x1, y1, x2, y2 = cubicle
        
        # Update unallocated space
        unallocated_space -= (x2 - x1 + 1) * (y2 - y1 + 1)
        
        # Update contested space
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if office_space[y][x] == 1:
                    contested_space += 1
                else:
                    office_space[y][x] = 1
    
    # Print the results
    print(f"Total {total_space}")
    print(f"Unallocated {unallocated_space}")
    print(f"Contested {contested_space}")
    
    # Print the uncontested space for each employee
    for employee, cubicle in cubicles.items():
        x1, y1, x2, y2 = cubicle
        uncontested_area = (x2 - x1 + 1) * (y2 - y1 + 1) - contested_space
        print(f"{employee} {uncontested_area}")

if __name__ == "__main__":
    main()

