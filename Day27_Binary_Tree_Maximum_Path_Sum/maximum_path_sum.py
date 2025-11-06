# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMax(self,node):
        if node==None:
            return 0,float('-inf')
        left_max_sum,left_ans=self.findMax(node.left)
        right_max_sum,right_ans=self.findMax(node.right)
        curr_ans=max(node.val,node.val+left_max_sum)
        curr_ans=max(curr_ans,curr_ans+right_max_sum)
        curr_ans=max(curr_ans,left_ans)
        curr_ans=max(curr_ans,right_ans)
        curr_sum=max(left_max_sum,right_max_sum)
        curr_sum=max(node.val,node.val+curr_sum)
        return curr_sum,curr_ans
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        temp,ans=self.findMax(root)
        return ans
        
