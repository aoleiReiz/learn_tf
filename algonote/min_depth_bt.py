#Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        q = deque()
        ans = 0
        if root:
            q.append(root)
            ans += 1
            while q:
                size = len(q)
                for _ in range(size):
                    node = q.popleft()
                    if node.left is None and node.right is None:
                        return ans
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5
    print(s.minDepth(node1))