# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDiameter(self,node):
        if node==None:
            return 0,0
        left_max_depth,ans_left=self.findDiameter(node.left)
        right_max_depth,ans_right=self.findDiameter(node.right)
        ans=(left_max_depth+right_max_depth)
        ans=max(ans,ans_left)
        ans=max(ans,ans_right)
        return max(left_max_depth,right_max_depth)+1,ans
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        depth,ans=self.findDiameter(root)
        return ans
        
