import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree(object):
    def __init__(self):
        self.root = None

    def create_tree(self, expr):
        tokens = expr.split()
        stack = Stack()
        current_node = Node()
        self.root = current_node

        for token in tokens:
            if token == '(':
                new_node = Node()
                current_node.lChild = new_node
                stack.push(current_node)
                current_node = new_node
            elif token in operators:
                current_node.data = token
                stack.push(current_node)
                new_node = Node()
                current_node.rChild = new_node
                current_node = new_node
            elif token == ')':
                if not stack.is_empty():
                    current_node = stack.pop()
            else:  # Operand
                current_node.data = float(token)  # Use float instead of int
                current_node = stack.pop() if not stack.is_empty() else current_node

    def evaluate(self, aNode):
        if aNode.data is None:
            return None
        if isinstance(aNode.data, (int, float)):
            return float(aNode.data)
        left_value = self.evaluate(aNode.lChild)
        right_value = self.evaluate(aNode.rChild)

        operator = aNode.data
        if operator == '+':
            return left_value + right_value
        elif operator == '-':
            return left_value - right_value
        elif operator == '*':
            return left_value * right_value
        elif operator == '/':
            return left_value / right_value
        elif operator == '//':
            return left_value // right_value
        elif operator == '%':
            return left_value % right_value
        elif operator == '**':
            return left_value ** right_value

    def pre_order(self, aNode):
        if aNode is None:
            return ''
        result = str(aNode.data) + ' '
        result += self.pre_order(aNode.lChild)
        result += self.pre_order(aNode.rChild)
        return result

    def post_order(self, aNode):
        if aNode is None:
            return ''
        result = self.post_order(aNode.lChild)
        result += self.post_order(aNode.rChild)
        result += str(aNode.data) + ' '
        return result

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
