# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs_sum(self, node, total):
        if node.left == None and node.right == None:
            return total
        elif node.left == None:
            return self.dfs_sum(node.right, total*10+node.right.val)
        elif node.right == None:
            return self.dfs_sum(node.left, total*10+node.left.val)
        else:
            return self.dfs_sum(node.left, total*10+node.left.val) + self.dfs_sum(node.right, total*10+node.right.val)
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return(self.dfs_sum(root, root.val))
        
        