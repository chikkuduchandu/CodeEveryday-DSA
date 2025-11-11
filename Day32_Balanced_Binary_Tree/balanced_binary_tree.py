# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def checkBalanced(self,node):
        if node==None:
            return True,0
        res1,left_len=self.checkBalanced(node.left)
        res2,right_len=self.checkBalanced(node.right)
        if res1==False or res2==False:
            return False,0
        if abs(left_len - right_len)>1:
            return False,0
        return True,max(left_len,right_len)+1

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        res,depth=self.checkBalanced(root)
        return res
        
