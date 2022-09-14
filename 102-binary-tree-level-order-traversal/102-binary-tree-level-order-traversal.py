# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root == None:
            return []
        return(self.bfs(root))
    def bfs(self,node):
        result = []
        queue_now = []
        queue_now.append(node)
        queue_later = []
        current_block = []
        while queue_now or queue_later:
            current = queue_now.pop(0)
            current_block.append(current.val)
            if current.left:
                queue_later.append(current.left)
            if current.right:
                queue_later.append(current.right)
            if not queue_now:
                result.append(current_block)
                current_block = []
                queue_now = queue_later
                queue_later = []
        return result