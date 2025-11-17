# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,node,values):
        if node==None:
            return
        self.inorder(node.left,values)
        values.append(node.val)
        self.inorder(node.right,values)
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        values=[]
        self.inorder(root,values)
        
        return values[k-1]
        
    
        

        
