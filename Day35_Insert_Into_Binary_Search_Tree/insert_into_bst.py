# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insert(self,node,val):
        if node.val<val:
            if node.right==None:
                node.right=TreeNode(val)
            else:
                self.insert(node.right,val)
        else:
            if node.left==None:
                node.left=TreeNode(val)
            else:
                self.insert(node.left,val)
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root==None:
            return TreeNode(val)
        self.insert(root,val)
        return root
        
