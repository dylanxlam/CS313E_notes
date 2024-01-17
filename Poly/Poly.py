
#  File: Poly.py

#  Description: This Python code defines a linked list-based representation of polynomials, 
        #  with functionalities to insert terms in descending order of exponents, 
        #  perform polynomial addition, multiplication, and output the results.

#  Student Name: Alexander Romero-Barrionuevo

#  Student UT EID: ANR3784

#  Partner Name:  Dylan Lam

#  Partner UT EID: DXL85

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created: 11/7/23

#  Date Last Modified: 11/10/23

import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
        self.first = None

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        new_link = Link(coeff, exp)
        if self.first is None:
            self.first = new_link
        else:
            current = self.first
            previous = None
            while current is not None and current.exp > exp:
                previous = current
                current = current.next

            if current is not None and current.exp == exp:
                # If a term with the same exponent exists, add coefficients
                current.coeff += coeff
                if current.coeff == 0:
                    # If the sum is zero, remove the term
                    if previous is None:
                        self.first = current.next
                    else:
                        previous.next = current.next
                else:
                    # Otherwise, update the coefficient
                    current.coeff = current.coeff
            else:
                # Insert the new term
                new_link.next = current
                if previous is None:
                    self.first = new_link
                else:
                    previous.next = new_link

    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        result = LinkedList()
        current_self = self.first
        current_p = p.first

        while current_self is not None or current_p is not None:
            if current_self is not None and current_p is not None:
                if current_self.exp == current_p.exp:
                    # If exponents are equal, add coefficients and insert the term
                    sum_coeff = current_self.coeff + current_p.coeff
                    if sum_coeff != 0:
                        result.insert_in_order(sum_coeff, current_self.exp)
                    current_self = current_self.next
                    current_p = current_p.next
                elif current_self.exp > current_p.exp:
                    # If exponent in the first polynomial is greater, insert the term from the first polynomial
                    result.insert_in_order(current_self.coeff, current_self.exp)
                    current_self = current_self.next
                else:
                    # If exponent in the second polynomial is greater, insert the term from the second polynomial
                    result.insert_in_order(current_p.coeff, current_p.exp)
                    current_p = current_p.next
            elif current_self is not None:
                # If there are remaining terms in the first polynomial, insert them
                result.insert_in_order(current_self.coeff, current_self.exp)
                current_self = current_self.next
            else:
                # If there are remaining terms in the second polynomial, insert them
                result.insert_in_order(current_p.coeff, current_p.exp)
                current_p = current_p.next

        # Combine terms with the same exponent in the result
        current_result = result.first
        while current_result is not None and current_result.next is not None:
            if current_result.exp == current_result.next.exp:
                current_result.coeff += current_result.next.coeff
                current_result.next = current_result.next.next
            else:
                current_result = current_result.next

        return result

    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        result = LinkedList()
        current_self = self.first

        while current_self is not None:
            current_p = p.first
            while current_p is not None:
                new_coeff = current_self.coeff * current_p.coeff
                new_exp = current_self.exp + current_p.exp
                if new_coeff != 0:  # Exclude terms with coefficient 0
                    result.insert_in_order(new_coeff, new_exp)
                current_p = current_p.next
            current_self = current_self.next

        # Combine terms with the same exponent in the result
        current_result = result.first
        while current_result is not None and current_result.next is not None:
            if current_result.exp == current_result.next.exp:
                current_result.coeff += current_result.next.coeff
                current_result.next = current_result.next.next
            else:
                current_result = current_result.next

        return result

    # create a string representation of the polynomial
    def __str__ (self):
        result = []
        current = self.first
        while current is not None:
            result.append(str(current))
            current = current.next
        return ' + '.join(result)

def main():
    # Read the number of terms in the first polynomial (p)
    n = int(sys.stdin.readline().strip())

    # Create the first polynomial (p)
    p = LinkedList()
    for _ in range(n):
        coeff, exp = map(int, sys.stdin.readline().strip().split())
        p.insert_in_order(coeff, exp)

    # Skip the blank line
    sys.stdin.readline()

    # Read the number of terms in the second polynomial (q)
    m = int(sys.stdin.readline().strip())

    # Create the second polynomial (q)
    q = LinkedList()
    for _ in range(m):
        coeff, exp = map(int, sys.stdin.readline().strip().split())
        q.insert_in_order(coeff, exp)

    # Get the sum of p and q and print the sum
    sum_result = p.add(q)
    print(sum_result)

    # Get the product of p and q and print the product
    product_result = p.mult(q)
    print(product_result)

if __name__ == "__main__":
  main()