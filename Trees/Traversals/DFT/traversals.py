class Node:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)


class Tree:
    '''

    THE TREE STRUCTURE USED IN THIS FILE IS:

               4
        2            6
     1     3      5     7

    '''
    def __init__(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        n6 = Node(6)
        n7 = Node(7)
        
        n4.left = n2
        n2.left = n1
        n2.right = n3
        n4.right = n6
        n6.left = n5
        n6.right = n7

        self.root = n4

    def __str__(self):
        return str(self.root.val)

    def __repr__(self):
        return str(self)


def recursive_preorder(root: Node) -> list:
    '''
    Time: O(n)
    Space: O(h)
    '''
    def helper(root, res):
        if root is None:
            return
        res.append(root)
        helper(root.left, res)
        helper(root.right, res)
    res = []
    helper(root, res)
    return res


def iterative_preorder(root: Node) -> list:
    '''
    Time: O(n)
    Space: O(h)
    '''
    if not root:
        return []

    res = []
    stack = [root]
    while stack:
        root = stack.pop()
        res.append(root)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return res


def recursive_inorder(root: Node) -> list:
    '''
    Time: O(n)
    Space: O(h)
    '''
    def helper(root, res):
        if root is None:
            return
        helper(root.left, res)
        res.append(root)
        helper(root.right, res)
    res = []
    helper(root, res)
    return res


def iterative_inorder(root: Node) -> list:
    '''
    Time: O(n)
    Space: O(h)
    '''
    res = []
    stack = []
    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            root = stack.pop()
            res.append(root)
            root = root.right
    return res


def recursive_postorder(root: Node) -> list:
    '''
    Time: O(n)
    Space: O(h)
    '''
    def helper(root, res):
        if root is None:
            return
        helper(root.left, res)
        helper(root.right, res)
        res.append(root)
    res = []
    helper(root, res)
    return res


def iterative_postorder1(root: Node) -> list:
    '''
    Uses 1 stack
    Time: O(n)
    Space: O(h)
    '''
    res = []
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            if stack[-1].right:
                root = stack[-1].right
            else:
                node = stack.pop()
                res.append(node)
                while stack and node is stack[-1].right:
                    node = stack.pop()
                    res.append(node)
    return res


def iterative_postorder2(root: Node) -> list:
    '''
    Uses 2 stacks
    Time: O(n)
    Space: O(n)
    '''
    if not root:
        return []

    res = []
    stack1 = [root]
    stack2 = []
    while stack1:
        root = stack1.pop()
        stack2.append(root)
        if root.left:
            stack1.append(root.left)
        if root.right:
            stack1.append(root.right)
    while stack2:
        res.append(stack2.pop())
    return res


def morris_inorder_traversal(root: Node):
    '''
    Time: O(n)
    Space: O(1)
    '''
    def findPredecessor(root: Node):
        curr = root.left
        while curr.right and curr.right != root:
            curr = curr.right
        return curr

    res = []
    while root:
        if root.left:
            predecessor = findPredecessor(root)
            if predecessor.right:
                predecessor.right = None
                res.append(root)
                root = root.right
            else:
                predecessor.right = root
                root = root.left
        else:
            res.append(root)
            root = root.right
    return res


if __name__ == '__main__':
    root = Tree().root

    # PREORDER
    print('PREORDER')
    print(iterative_preorder(root))
    print(recursive_preorder(root))
    print()
    print()

    # INORDER
    print('INORDER')
    print(recursive_inorder(root))
    print(iterative_inorder(root))
    print()
    print()

    # POSTORDER
    print('POSTORDER')
    print(recursive_postorder(root))
    print(iterative_postorder1(root))
    print(iterative_postorder2(root))
    print()
    print()


    # MORRIS
    print('MORRIS INORDER')
    print(morris_inorder_traversal(root))
    print()
    print()
