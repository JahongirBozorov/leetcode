# 1-misol
import collections
from idlelib.tree import TreeNode
from typing import Optional


def isBalanced(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True

    def height(root):
        if not root:
            return 0
        return 1 + max(height(root.left), height(root.right))

    left, right = height(root.left), height(root.right)
    if abs(left - right) <= 1:
        return True and isBalanced(root.left) and isBalanced(root.right)
    return False

# bu misolda yechimni leetcode yechildi treeni bu yerda qanday yozishni bilmadim


# 2-misol

def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    left = minDepth(root.left) if root.left else float('inf')
    right = minDepth(root.right) if root.right else float('inf')
    return 1 + min(left, right)

# 1 va 2 - misolda funksiya chaqirilganda oldiga self. qo'ying leetcodda tekshirayotganda

# 3-misol

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    queue = collections.deque([(root, root.val)])
    while queue:
        node, val = queue.popleft()
        if not node.left and not node.right:
            if val == targetSum:
                return True
            else:
                continue
        if node.left:
            queue.append((node.left, val + node.left.val))
        if node.right:
            queue.append((node.right, val + node.right.val))
    return False