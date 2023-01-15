class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # 1. Find Minimum Element (Exercise)
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    # 2. Find Maximum Element (Exercise)
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # 3. Calculate Sum of All Elements (Exercise)
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    # 4. Performs Post Order Traversal (Exercise)
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    # 5. Performs Pre Order Traversal (Exercise)
    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    # Example 1
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())

    # Example 2
    print(numbers_tree.search(20))

    # Example 3
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("Uk is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    # Example 4
    print(country_tree.in_order_traversal())

    # Running Exercises
    print("The Minimum Element is:", numbers_tree.find_min())
    print("The Maximum Element is:", numbers_tree.find_max())
    print("The Sum of all Elements is:", numbers_tree.calculate_sum())
    print("Post Order Traversal:", numbers_tree.post_order_traversal())
    print("Pre Order Traversal:", numbers_tree.pre_order_traversal())

    # Demo using the letters of my fullname as the content of the binary tree
    full_name = ["R", "O", "M", "A", "R", "K", "C", "P", "I", "Ñ", "E", "R", "O"]
    name_tree = build_tree(full_name)
    print("Is letter A in the list?", name_tree.search("A"))
    print("Pre Order Traversal of the list:", name_tree.pre_order_traversal())
    print("In Order Traversal list of Full Name:", name_tree.in_order_traversal())
    print("Post Order Traversal of the list:", name_tree.post_order_traversal())
    # Can't Use Minimum, Maximum, and Sum as the content of Binary Tree are strings
