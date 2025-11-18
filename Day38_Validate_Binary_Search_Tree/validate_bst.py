# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkFunc(self,node,left,right):
        if node==None:
            return True
        if node.val<=left or node.val>=right:
            
            return False
        return ( self.checkFunc(node.left,left,node.val) and self.checkFunc(node.right,node.val,right))
        
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        res=self.checkFunc(root,float('-inf'),float('inf'))
        return res
        


        
