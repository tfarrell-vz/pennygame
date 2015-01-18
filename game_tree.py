import random

class GameNode:
    def __init__(self, num_pennies, left=None, middle=None, right=None):
        self.num_pennies = num_pennies
        self.left, self.middle, self.right = left, middle, right

    def is_leaf(self):
        """
        Determines if a node is a leaf. A GameNode leaf is one that has 0 pennies. It also shouldn't be connecting
        to any other nodes, as the edges represent removal of pennies.
        """
        if self.num_pennies == 0:
            return True

        else:
            return False

    def num_leaves(self):
        """
        Yields the number of leaves by recursively adding their count.
        """
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
        """
        Returns the first node, the root of the tree, after having created the entire tree recursively.
        """
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

    def pennies_on_table(self):
        """
        Retrieves the current number of pennies on the table.
        """
        return self._game_position.num_pennies

    def ways_to_play(self):
        """ Yields how many games are possible given the starting number of pennies."""
        return self._root.num_leaves()

    def remove_pennies(self, pennies):
        """
        Removes pennies from the table by moving the game position down the tree in the appropriate fashion.
        Left move is removing 1 penny.
        Middle move is removing 2 pennies.
        Right move is removing 3 pennies.
        """
        if pennies > self.pennies_on_table():
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
    """
    Obtains a number of pennies from the user to build the game tree.
    """
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

def computer_move(mode, pennies):
    move_list = {1: 1,
                 2: 1,
                 3: 2,
                 4: 3,
                 5: random.randrange(1,4),
                 6: 1,
                 7: 2,
                 8: 3
    }
    if mode == 'expert':
        return move_list.get(pennies, random.randrange(1,4))

    else:
        if pennies >= 4:
            return random.randrange(1, 4)

        else:
            return random.randrange(1, pennies+1)


def main():
    print("Welcome to the Penny Game!")
    pennies = get_pennies()
    tree = GameTree(pennies)
    print("Number of ways to play: ", tree.ways_to_play())
    mode = input(">> Select normal or expert: ")

    random.seed()
    victor = ""

    while tree.pennies_on_table() > 0:
        # Announce pennies on table.
        # Computer makes a move.
        # Check if game is over.
        # Human makes a move.
        # Check if game is over.

        pennies_on_table = tree.pennies_on_table()
        print("Number of pennies on the table: ", pennies_on_table)

        computer = computer_move(mode, pennies_on_table)
        print("Computer removes %s pennies" % computer)
        tree.remove_pennies(computer)

        if tree.pennies_on_table() == 0:
            victor = "Human"
            break

        print("Number of pennies on the table: ", tree.pennies_on_table())

        while True:
            try:
                human_move = int(input(">> How many pennies will you remove?: "))
                if 1 <= human_move <= 3 and human_move <= tree.pennies_on_table():
                    tree.remove_pennies(human_move)
                    break
                else:
                    print("Be careful! Try again . . .")
            except ValueError:
                print("Invalid number of pennies.")
        if tree.pennies_on_table() == 0:
            victor = "Computer"
            break

    if victor == "Human":
        print("\nCongratulations, you won!")

    elif victor == "Computer":
        print("\nYOU LOST! All hail The Computer")

    else:
        print("Game indeterminate due to programmer error.")




if __name__ == '__main__':
    main()


