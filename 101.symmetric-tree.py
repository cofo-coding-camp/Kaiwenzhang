#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Method 1 
    # Recursion
    # Time: O(n)
    # Space: O(n) - when tree is linear
    # def isSymmetric(self, root: TreeNode) -> bool:

    #     if not root:
    #         return True

    #     res = [True]
    #     self.dfs(root.left, root.right, res)

    #     return res[0]

    # def dfs(self, left: TreeNode, right: TreeNode, res: List[bool]):

    #     # base case
    #     # reach the end
    #     if left == None and right == None:
    #         return
        
    #     # left and right are different
    #     if left == None or right == None:
    #         res[0] = False
    #         return

    #     # left and right are different
    #     if left.val != right.val:
    #         res[0] = False
    #         return
     
    #     # at the point, both left and right are not null
    #     # thus it is safe to call node.left node.right
    #     self.dfs(left.left, right.right, res)
    #     self.dfs(left.right, right.left, res)

    # Method 2
    # iterative
    # 双端队列
    # Time: O(n)
    # Space: O(n)
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        q = []
        q.append(root)
        q.append(root)
        
        while len(q) > 0:
            node_1 = q.pop(0)
            node_2 = q.pop(0)

            if node_1 == None and node_2 == None:
                continue
            if node_1 == None or node_2 == None:
                return False
            if node_1.val != node_2.val:
                return False

            q.append(node_1.left)
            q.append(node_2.right)
            q.append(node_1.right)
            q.append(node_2.left)

        return True


# @lc code=end

