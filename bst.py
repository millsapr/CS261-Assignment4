# Course: CS261 - Data Structures
# Student Name: Ryan Millsap
# Assignment: 4
# Description: Implements a binary search tree (BST) class with various methods.


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
        new_node = TreeNode(value)                              # create a new node with value

        if self.root is None:                                   # if empty tree, new node becomes root
            self.root = new_node
        else:
            parent = None
            cur = self.root                                     # otherwise, start at root
            while cur is not None:                              # find an open space
                parent = cur                                    # keep track of previous node; it will be parent
                if new_node.value < cur.value:
                    cur = cur.left                              # if value is less, go left
                else:
                    cur = cur.right                             # if value is greater, go right
            if new_node.value < parent.value:                   # assign new node to appropriate side of previous node,
                parent.left = new_node                              # which is now parent
            else:
                parent.right = new_node

    def contains(self, value: object) -> bool:
        """
        returns True if the value parameter is in the BinaryTree or False if it is not in
        the tree. If the tree is empty, the method returns False.
        """
        if self.root is None:                                   # empty tree contains no values
            return False

        cur = self.root                                         # start at root
        while cur is not None:                                  # traverse tree until end reached
            if cur.value == value:
                return True                                     # if value found, tree contains it
            elif value < cur.value:
                cur = cur.left                                  # if value less than current node, go left
            else:
                cur = cur.right                                 # if value greater, go right
        return False                                            # if end reached without finding value, not contained

    def get_first(self) -> object:
        """
        returns the value stored at the root node. If the BinaryTree is empty, returns None.
        """
        if self.root is None:                                   # if empty return None
            return None
        else:
            return self.root.value                              # return root value

    def remove_first(self) -> bool:
        """
        removes the root node in the BinaryTree. Returns False if the tree is
        empty and there is no root node to remove and True if the root is removed.
        """
        if self.root is None:                                   # if tree is empty, return False
            return False

        if self.root.left is None and self.root.right is None:
            self.root = None                                    # if only one node in tree, remove root and you're done

        elif self.root.right is None:                           # if root only has left child, replace root with that
            self.root = self.root.left                              # no other changes needed

        else:       
            """find in-order successor to replace root"""
            S = self.root.right                                 # start with right child as potential successor
            # PS = S
            n_right = 1                                         # flag for whether root.right is successor
            while S.left is not None:                           # until bottom-leftmost child is reached
                PS = S                                          # track previous node as parent to successor
                S = S.left                                      # move to next left child
                n_right = 0                                     # if there are left children, successor not root.right
            S.left = self.root.left                             # successor moves up to get left child of root
            if n_right == 0:                                    # if successor was not root.right
                PS.left = S.right                                   # successor's right child take's successor's place
                S.right = self.root.right                           # successor gets right child of root
            # S.left = self.root.left
            self.root = S                                       # successor becomes root
        
        return True

    def remove(self, value) -> bool:
        """
        removes the first instance of the object in the BinaryTree. returns True if the value is
        removed from the BinaryTree and otherwise returns False.
        """
        if self.contains(value) is False:                   # if value not in tree, return False
            return False                                    

        if self.root is None:                               # if tree is empty, return False
            return False

        if self.root.value == value:                        # if root is target value, just use remove_first
            self.remove_first()
            return True

        cur = self.root                                     # find N by starting at root
        PN = None                                           # start tracking parent of N

        while cur is not None:                              # find node to be removed and its parent
            if cur.value == value:                          # once value is found, that's your node. break loop.
                N = cur
                break
            elif value < cur.value:                         # if value is less than current node:
                PN = cur                                        # update parent each time to previous node
                cur = cur.left                                  # go left
                left_child = 1                               # track whether node was a left child of parent
            else:
                PN = cur                                    # if value is greater than or equal:
                cur = cur.right                                 # go right
                left_child = 0                                  # record that node is right child

        if N.left is None and N.right is None:              # no children (by the mountain goats)
            if left_child == 1:
                PN.left = None                              # if N was a left child, point parent.left to none
            else:
                PN.right = None                             # otherwise, point parent.right to none

        elif N.right is None:                               # if N has no right child:
            if left_child == 1:                                 # if N was parent's left child
                PN.left = N.left                                # replace N with it's own left child
            else:
                PN.right = N.left                           # similar if N was parent's right child

        else:
            """find in-order successor to replace N; similar to corresponding section in remove_first"""
            S = N.right
            PS = S
            n_right = 1
            while S.left is not None:
                PS = S
                S = S.left
                n_right = 0
            S.left = N.left

            if n_right == 0:
                PS.left = S.right
                S.right = N.right

            if left_child != 0:
                PN.left = S
            else:
                PN.right = S

        N.left = None                                       # free N so that it points at nothing
        N.right = None

        return True

    def pre_order_traversal(self) -> Queue:
        """
        performs a pre-order traversal and returns a Queue object that contains values of the visited nodes,
        in the order they were visited
        """
        q = Queue()                                         # create empty queue to record each node
        self.pre_order_traversal_helper(self.root, q)       # start recursive call with root and empty queue
        return q                                            # return queue once it's complete

    def pre_order_traversal_helper(self, cur, q) -> Queue:
        """
        helper method for pre_order_traversal. borrowed from _str_helper above.
        """
        if cur is None:                                     # base case
            return

        q.enqueue(str(cur.value))                           # enqueue value of current node
        self.pre_order_traversal_helper(cur.left, q)        # recursive case for left subtree
        self.pre_order_traversal_helper(cur.right, q)       # recursive case for right subtree

    def in_order_traversal(self) -> Queue:
        """
        performs an in-order traversal and returns a Queue object that contains values of the visited nodes,
        in the order they were visited
        """
        q = Queue()
        self.in_order_traversal_helper(self.root, q)
        return q

    def in_order_traversal_helper(self, cur, q) -> Queue:
        """
        helper method for in_order_traversal. borrowed from _str_helper above.
        """
        if cur is None:                                     # base case
            return

        self.in_order_traversal_helper(cur.left, q)         # recursive case for left subtree
        q.enqueue(str(cur.value))                           # enqueue value of current node
        self.in_order_traversal_helper(cur.right, q)        # recursive case for right subtree

    def post_order_traversal(self) -> Queue:
        """
        performs a post-order traversal and returns a Queue object that contains values of the visited nodes,
        in the order they were visited
        """
        q = Queue()
        self.post_order_traversal_helper(self.root, q)
        return q

    def post_order_traversal_helper(self, cur, q) -> Queue:
        """
        helper method for post_order_traversal. borrowed from _str_helper above.
        """
        if cur is None:                                     # base case
            return

        self.post_order_traversal_helper(cur.left, q)       # recursive case for left subtree
        self.post_order_traversal_helper(cur.right, q)      # recursive case for right subtree
        q.enqueue(str(cur.value))                           # enqueue value of current node

    def by_level_traversal(self) -> Queue:
        """
        performs a by-level traversal and returns a Queue object that contains values of the visited nodes,
        in the order they were visited
        """
        q = Queue()                                         # create empty queue to store to-be-processed nodes
        visited = Queue()                                   # create empty queue to store values of processed nodes
        q.enqueue(self.root)                                # start with root

        while q.is_empty() is False:                        # until all nodes have been processed
            cur = q.dequeue()                               # take next node in queue
            if cur is not None:
                visited.enqueue(cur.value)                  # add its value to visited queue
                q.enqueue(cur.left)                         # add its children to queue for processing
                q.enqueue(cur.right)
        return visited                                      # return queue of node values

    def is_full(self) -> bool:
        """
        returns True if the current tree is a ‘full binary tree’. Empty tree is
        considered ‘full’. Tree consisting of a single root node is ‘full’
        """
        q = Queue()                                         # create queue to store nodes in pre-order order
        self.is_full_helper(self.root, q)                   # recursive call similar ot pre-order traversal

        while q.is_empty() is False:                        # look at every interior node in queue
            cur = q.dequeue()                                   # if any of them only have one child, not full
            if (cur.left is None and cur.right is not None) or (cur.left is not None and cur.right is None):
                return False

        return True                                         # otherwise the tree is full

    def is_full_helper(self, cur, q):
        """
        helper method for is_full. borrowed from _str_helper/pre_order_traversal above.
        """
        if cur is None:                                     # base case
            return

        q.enqueue(cur)                                      # enqueue current node
        self.is_full_helper(cur.left, q)                    # recursive case for left subtree
        self.is_full_helper(cur.right, q)                   # recursive case for right subtree

    def is_complete(self) -> bool:
        """
        returns True if the current tree is a ‘complete binary tree’. Empty tree is
        considered complete. Tree consisting of a single root node is complete.
        """
        if self.root is None:                                   # empty tree counts as Complete
            return True

        two_kids = 1                                            # track whether any given node has two children
                                                                   # if not, check for children of other nodes on level

        """use a variation on the by_level_traversal to check nodes at each depth """
        q = Queue()                                             # create queue to track which nodes to check next
        q.enqueue(self.root)                                    # start with root
        while q.is_empty() is False:
            cur = q.dequeue()

            if cur.left is not None:                            # check if node has left child
                if two_kids == 0:                               # if another node on same level didn't have two children
                    return False                                    # tree is not complete
                q.enqueue(cur.left)                             # add left child to queue
            else:
                two_kids = 0                                    # if no left child, node is not full, so keep track

            if cur.right is not None:                           # similarly for right child
                if two_kids == 0:
                    return False
                q.enqueue(cur.right)
            else:
                two_kids = 0
                                                                # if whole tree traversed without children on levels
        return True                                                 # below not full nodes, tree is complete

    def is_perfect(self) -> bool:
        """
        returns True if the current tree is a ‘perfect binary tree’. Empty tree is
        considered ‘perfect’. Tree consisting of a single root node is ‘perfect
        """
        if self.is_full() is False:                             # if tree is not full, it can't be perfect
            return False

        h = self.height()                                       # get height of tree
        total_nodes = 1                                         # start with 1 so not muliplying by 0

        """use total nodes = 2^(h+1)-1 fact about perfect binary tree"""
        while h > -1:                                           # for every level in tree
            total_nodes = total_nodes * 2                           # multiply total nodes by 2
            h -= 1
        total_nodes -= 1
        if self.size() != total_nodes:                          # if size of tree not equal to this calculation based
            return False                                            # on height, tree is not perfect

        return True                                             # if they're equal, it is perfect yay

    def size(self) -> int:
        """
        returns the total number of nodes in the tree
        """
        q = self.in_order_traversal()                           # use traversal to create queue of nodes
        count = 0

        while q.is_empty() is False:                            # keep count as each node is removed from queue
            q.dequeue()
            count += 1

        return count                                            # count is the size of the tree

    def height(self) -> int:
        """
        returns the height of the binary tree. Empty tree has a height of -1. Tree consisting of
        just a single root node returns a height of 0
        """
        return self.height_helper(self.root)

    def height_helper(self, cur):
        """
        helper method for height
        """
        if cur is None:                                         # base case. empty tree has height of -1
            return -1
        else:
            left_height = self.height_helper(cur.left)          # recursive case for finding left depth
            right_height = self.height_helper(cur.right)        # recursive case for finding right depth
            return max(left_height + 1, right_height + 1)       # whichever is greater is the height
                                                                    # plus 1 because of root

    def count_leaves(self) -> int:
        """
        returns the number of nodes in the tree that have no children. If the tree is empty, returns 0
        """
        q = Queue()                                             # create empty queue to be filled recursively
        count = 0                                               # start a count
        self.count_leaves_helper(self.root, q)                  # recursive call to helper method

        while q.is_empty() is False:                            # check each node one at a time
            cur = q.dequeue()
            if cur.left is None and cur.right is None:          # if node has no children (by the mountain goats)
                count += 1                                          # increment count

        return count                                            # count is the number of childless leaves

    def count_leaves_helper(self, cur, q):
        """
        helper method for count_leaves. similar to in_order_traversal
        """
        if cur is None:                                         # base case
            return

        q.enqueue(cur)                                          # enqueue current node
        self.count_leaves_helper(cur.left, q)                   # recursive case for left subtree
        self.count_leaves_helper(cur.right, q)                  # recursive case for right subtree

    def count_unique(self) -> int:
        """
        returns the count of unique values stored in the tree.
        """
        q = self.in_order_traversal()                           # create sorted queue of all values
        prev = None                                             # start tracking previous value
        count = 0                                               # start count

        while q.is_empty() is False:                            # check each value one at a time
            cur = q.dequeue()
            if cur != prev:                                     # if value is not same as one before it
                count += 1                                          # increment unique count
            prev = cur                                          # current becomes previous for next check

        return count



# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

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
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

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

    """ remove() example 6 (gradescope) """
    print("\nPDF - method remove() example 6")
    print("-------------------------------")
    tree = BST(['TG', 'D', 'I', 'W', 'V', 'TG', 'WY'])
    print(tree.remove("V"))
    print(tree)

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

