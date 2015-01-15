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

class GameTree:
    def __init__(self, num_pennies):
        self._root = self.make_node(num_pennies)
        self._game_position = self._root

    def make_node(self, num_pennies):
        if num_pennies >= 3:
            node = GameNode(num_pennies, left=self.make_node(num_pennies-1), middle=self.make_node(num_pennies-2),
                            right=self.make_node(num_pennies-3))
            return node

        if num_pennies == 2:
            node = GameNode(num_pennies, left=self.make_node(num_pennies-1),
                            middle=self.make_node(num_pennies-2))

            return node

        if num_pennies == 1:
            node = GameNode(num_pennies, left=self.make_node(num_pennies-1))
            return node

        if num_pennies == 0:
            node = GameNode(num_pennies)
            return node

    def ways_to_play(self):
        """ Yields how many games are possible given the starting number of pennies."""
        return self._root.num_leaves()

    def remove_pennies(self, pennies):
        if pennies > self._game_position.num_pennies:
            print("Not enough pennies on the table.")

        if 1 <= pennies <= 3:
            if pennies == 1:
                self._game_position = self._game_position.left

            elif pennies == 2:
                self._game_position = self._game_position.middle

            elif pennies == 3:
                self._game_position = self._game_position.right

        else:
            print("Illegal move, cheater.")

def get_pennies():
    accepted = False
    while not accepted:
        try:
            pennies = int(input(">> Enter the number of pennies to start the game (>=5): "))
        except ValueError:
            print("That wasn't a number, try again.\n")

        if pennies >= 5:
            accepted = True
        else:
            print("You need to choose 5 or more pennies to play.\n")
    return pennies


def main():
    print("Welcome to the Penny Game!")
    pennies = get_pennies()
    tree = GameTree(pennies)
    print("Number of ways to play: ", tree.ways_to_play())


if __name__ == '__main__':
    main()


