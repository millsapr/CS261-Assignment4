# Course: CS261 - Data Structures
# Student Name: Ryan Millsap
# Assignment: 4
# Description: Implements a binary search tree (BST) class with various methods


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        adds a new value to the tree, maintaining BST property. Duplicates are allowed and are
        placed in the right subtree
        """
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
        else:
            parent = None
            cur = self.root
            while cur is not None:
                parent = cur
                if new_node.value < cur.value:
                    cur = cur.left
                else:
                    cur = cur.right
            if new_node.value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node

    def contains(self, value: object) -> bool:
        """
        returns True if the value parameter is in the BinaryTree or False if it is not in
        the tree. If the tree is empty, the method returns False.
        """
        if self.root is None:
            return False

        cur = self.root
        while cur is not None:
            if cur.value == value:
                return True
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def get_first(self) -> object:
        """
        returns the value stored at the root node. If the BinaryTree is empty, returns None.
        """
        if self.root is None:
            return None
        else:
            return self.root.value

    def remove_first(self) -> bool:
        """
        removes the root node in the BinaryTree. Returns False if the tree is
        empty and there is no root node to remove and True if the root is removed.
        """
        if self.root is None:                               # if tree is empty, return False
            return False

        if self.root.left is None and self.root.right is None:
            self.root = None
        elif self.root.right is None:
            self.root = self.root.left
        else:
            successor = self.root.right
            parentSuccessor = successor
            nRight = 1                                     # IF S IS NOT N.RIGHT?
            while successor.left is not None:
                parentSuccessor = successor
                successor = successor.left
                nRight = 0
            print("successor is " + str(successor))
            successor.left = self.root.left
            if nRight != 1:
                parentSuccessor.left = successor.right
            successor.right = self.root.right
            successor.left = self.root.left
            self.root = successor
            # elif parent.left.value == self.root.value:
            #     print("target is a left child")
            #     parent.left = successor
            # else:
            #     print("target is a right child")
            #     parent.right = successor
        
        return True

    def remove(self, value) -> bool:
        """
        removes the first instance of the object in the BinaryTree. returns True if the value is
        removed from the BinaryTree and otherwise returns False.
        """
        if self.contains(value) is False:                   # if value not in tree, return False
            return False                                    # COME BACK AND CHECK AFTER TRAVERSAL METHODS

        if self.root is None:                               # if tree is empty, return False
            return False

        cur = self.root
        parent = None         # to fix GS test 'parent' ref'd before assignment
        while cur is not None:
            if cur.value == value:
                target = cur
                break
            elif value < cur.value:
                parent = cur
                cur = cur.left
            else:
                parent = cur
                cur = cur.right
        print("target is " + str(target))
        print("parent is " + str(parent))

        # print("parent.left.value = " + str(parent.left.value))
        # if N has no children point PN to None
        if target.left is None and target.right is None:
            print("no children")
            if parent.left is not None and parent.left.value == target.value:
                print("target is a left child")
                parent.left = None
            else:
                print("target is a right child")
                parent.right = None
        elif target.right is None:
            parent.right = target.left
            print("no target right child so parent right is " + str(parent.right))
        else:                                   # find IOS and PS
            # print("parent.left.value = " + str(parent.left.value))
            successor = target.right
            parentSuccessor = successor
            print("succ target.right is " + str(successor))
            nRight = 1
            while successor.left is not None:
                parentSuccessor = successor
                successor = successor.left
                nRight = 0
                print("nRight in while = " + str(nRight))
            print("successor is " + str(successor))
            print("nRight after while = " + str(nRight))
            successor.left = target.left
            print("parentSuccessor is " + str(parentSuccessor))
            if nRight != 1:
                print("nRight!=1")
                parentSuccessor.left = successor.right
                successor.right = target.right
                successor.left = target.left
                parent.right = successor
                print("parent.left is " + str(parent.left.value))
            elif parent is not None and parent.left is not None and parent.left.value == target.value:
                print("target is a left child")
                parent.left = successor
            else:
                print("target is a right child")
                # print("parent.right before reassign is " + str(parent.right))
                if parent is not None:
                    parent.right = successor
                else:
                    self.root = successor
                # print("parent.right after reassign is " + str(parent.right))
        target.left = None
        target.right = None
        # find successor (ios)
        return True


    def pre_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        return Queue()

    def in_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        return Queue()

    def post_order_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        return Queue()

    def by_level_traversal(self) -> Queue:
        """
        TODO: Write this implementation
        """
        return Queue()

    def is_full(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def is_complete(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def is_perfect(self) -> bool:
        """
        TODO: Write this implementation
        """
        return True

    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0

    def height(self) -> int:
        """
        TODO: Write this implementation
        """
        return -1

    def count_leaves(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0

    def count_unique(self) -> int:
        """
        TODO: Write this implementation
        """
        return 0



# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    # """ add() example #1 """
    # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # tree = BST()
    # print(tree)
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree)
    # tree.add(15)
    # tree.add(15)
    # print(tree)
    # tree.add(5)
    # print(tree)
    #
    # """ add() example 2 """
    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # tree = BST()
    # tree.add(10)
    # tree.add(10)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    # tree.add(5)
    # print(tree)
    # tree.add(-1)
    # print(tree)

    # """ contains() example 1 """
    # print("\nPDF - method contains() example 1")
    # print("---------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.contains(15))
    # print(tree.contains(-10))
    # print(tree.contains(15))
    #
    # """ contains() example 2 """
    # print("\nPDF - method contains() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print(tree.contains(0))
    #
    # """ get_first() example 1 """
    # print("\nPDF - method get_first() example 1")
    # print("----------------------------------")
    # tree = BST()
    # print(tree.get_first())
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree.get_first())
    # print(tree)
    #
    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    """ remove() example 4 (gradescope) """
    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    tree = BST([0, 1, 2, 2, 3, 3, 3])
    print(tree.remove(0))
    print(tree)
    print(tree.remove(2))
    print(tree)

    """ remove() example 5 (gradescope) """
    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    tree = BST([5, -4, -9, -9, -1, -3])
    print(tree.remove(-4))
    print(tree)

    # """ remove_first() example 1 """
    # print("\nPDF - method remove_first() example 1")
    # print("-------------------------------------")
    # tree = BST([10, 15, 5])
    # print(tree.remove_first())
    # print(tree)
    #
    # """ remove_first() example 2 """
    # print("\nPDF - method remove_first() example 2")
    # print("-------------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7])
    # print(tree.remove_first())
    # print(tree)

    # """ remove_first() example 3 """
    # print("\nPDF - method remove_first() example 3")
    # print("-------------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    # print(tree.remove_first(), tree)
    #
    # """ Traversal methods example 1 """
    # print("\nPDF - traversal methods example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    #
    # """ Traversal methods example 2 """
    # print("\nPDF - traversal methods example 2")
    # print("---------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    #
    # """ Comprehensive example 1 """
    # print("\nComprehensive example 1")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'  N/A {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print()
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    #
    # """ Comprehensive example 2 """
    # print("\nComprehensive example 2")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'N/A   {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in 'DATA STRUCTURES':
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print('', tree.pre_order_traversal(), tree.in_order_traversal(),
    #       tree.post_order_traversal(), tree.by_level_traversal(),
    #       sep='\n')

