import sys

class Link(object):
    def __init__(self, coeff=1, exp=1, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__(self):
        return '(' + str(self.coeff) + ', ' + str(self.exp) + ')'

class LinkedList(object):
    def __init__(self):
        self.first = None

    # keep Links in descending order of exponents
    def insert_in_order(self, coeff, exp):
        new_link = Link(coeff, exp)
        if self.first is None or exp > self.first.exp:
            new_link.next = self.first
            self.first = new_link
        else:
            current = self.first
            while current.next is not None and current.next.exp > exp:
                current = current.next
            if current.next is not None and current.next.exp == exp:
                current.next.coeff += coeff
            else:
                new_link.next = current.next
                current.next = new_link


    # add polynomial p to this polynomial and return the sum
    def add(self, p):
        result = LinkedList()
        current_p = p.first
        current_q = self.first

        while current_p is not None or current_q is not None:
            if current_p is None:
                result.insert_in_order(current_q.coeff, current_q.exp)
                current_q = current_q.next
            elif current_q is None:
                result.insert_in_order(current_p.coeff, current_p.exp)
                current_p = current_p.next
            elif current_p.exp > current_q.exp:
                result.insert_in_order(current_p.coeff, current_p.exp)
                current_p = current_p.next
            elif current_p.exp < current_q.exp:
                result.insert_in_order(current_q.coeff, current_q.exp)
                current_q = current_q.next
            else:
                result.insert_in_order(current_p.coeff + current_q.coeff, current_p.exp)
                current_p = current_p.next
                current_q = current_q.next

        return result


    def combine_like_terms(self):
        current = self.first
        while current is not None and current.next is not None:
            if current.exp == current.next.exp:
                current.coeff += current.next.coeff
                current.next = current.next.next
            else:
                current = current.next
        
    # multiply polynomial p to this polynomial and return the product
    def mult(self, p):
        result = LinkedList()

        current_p = p.first
        while current_p is not None:
            current_self = self.first
            while current_self is not None:
                coeff = current_p.coeff * current_self.coeff
                exp = current_p.exp + current_self.exp
                result.insert_in_order(coeff, exp)
                current_self = current_self.next

            current_p = current_p.next

        # Combine like terms with the same exponent in the result
        result.combine_like_terms()

        return result




    # create a string representation of the polynomial
    def __str__(self):
        result_str = ''
        current = self.first
        while current is not None:
            result_str += str(current)
            current = current.next
            if current is not None:
                result_str += ' + '
        return result_str

def main():
    # Format: n, (coeff, exp) pairs, blank line, m, (coeff, exp) pairs
    n = int(input())
    poly1 = LinkedList()
    for _ in range(n):
        coeff, exp = map(int, input().split())
        poly1.insert_in_order(coeff, exp)

    input()

    m = int(input())
    poly2 = LinkedList()
    for _ in range(m):
        coeff, exp = map(int, input().split())
        poly2.insert_in_order(coeff, exp)

    # get sum of p and q and print sum
    sum_result = poly1.add(poly2)
    print(sum_result)

    # get product of p and q and print product
    product_result = poly1.mult(poly2)
    print(product_result)

if __name__ == "__main__":
    main()
