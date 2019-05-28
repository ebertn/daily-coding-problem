# This problem was asked by Google.

# A unival tree (which stands for "universal 
# value") is a tree where all nodes under it 
# have the same value.

# Given the root to a binary tree, count the 
# number of unival subtrees.

# For example, the following tree has 5 unival 
# subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countUnival(root):
    if root.left is None and root.right is None:
        return 1
    elif root.left is None:
        return countUnival(root.right)
    elif root.right is None:
        return countUnival(root.left)
    elif root.left.val == root.val and root.right.val == root.val:
        return countUnival(root.left) + countUnival(root.right) + 1

    return countUnival(root.left) + countUnival(root.right)

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(countUnival(root))
root = Node('a', Node('a'), Node('a', Node('a'), Node('a', right=Node('A'))))
print(countUnival(root))

# Not totally finished, need to implement a case for determining 
# if the tree below is a valid unival