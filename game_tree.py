class GameNode:
    def __init__(self, num_pennies, left=None, middle=None, right=None):
        self.num_pennies = num_pennies
        self.left, self.middle, self.right = left, middle, right

    def is_leaf(self):
        if self.num_pennies == 0:
            return True

        else:
            return False

    def num_leaves(self):
        if self.is_leaf():
            return 1

        if self.left and self.middle and self.right:
            return self.left.num_leaves() + self.middle.num_leaves() + self.right.num_leaves()

        elif self.left and self.middle:
            return self.left.num_leaves() + self.middle.num_leaves()

        elif self.middle and self.right:
            return self.middle.num_leaves() + self.right.num_leaves()

        elif self.left and self.right:
            return self.left.num_leaves() + self.right.num_leaves()

        elif self.left and not self.middle and not self.right:
            return self.left.num_leaves()

        elif self.middle and not self.left and not self.right:
            return self.middle.num_leaves()

        elif self.right and not self.left and not self.middle:
            return self.right.num_leaves()

def main():
    first_node = GameNode(2)
    second_node = GameNode(1)
    third_node = GameNode(0)
    fourth_node = GameNode(0)

    first_node.left = second_node
    first_node.middle = third_node
    second_node.left = fourth_node

    print(first_node.num_leaves())


if __name__ == '__main__':
    main()


