# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def genDict(root):
    binary_dict = {'val': root.val}

    if root.left is not None:
        binary_dict['left'] = genDict(root.left)

    if root.right is not None:
        binary_dict['right'] = genDict(root.right)

    return binary_dict

def serialize(root):
    return json.dumps(genDict(root))

def buildTree(d):
    root = Node(d['val'])

    if 'left' in d:
        root.left = buildTree(d['left'])

    if 'right' in d:
        root.right = buildTree(d['right'])

    return root

def deserialize(s):
    return buildTree(json.loads(s))

# ------------------------- Testing ------------------------- #
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
assert deserialize(serialize(node)).left.left.val == 'left.left'
assert binaryTreeEquals(node, test)
print('Passed')
test = deserialize(serialize(node))

def printTree(root):
    if root is not None:
        print(root.val)
        printTree(root.left)
        printTree(root.right)

def binaryTreeEquals(tree1, tree2):
    if tree1.val != tree2.val:
        return False
        
    left_equal = False    
    if tree1.left is None and tree2.left is None:
        left_equal = True
    elif tree1.left and tree2.left:
        left_equal = binaryTreeEquals(tree1.left, tree2.left)

    right_equal = False
    if tree1.right is None and tree2.right is None:
        right_equal = True
    elif tree1.right and tree2.right:
        right_equal = binaryTreeEquals(tree1.right, tree2.right)

    return left_equal and right_equal