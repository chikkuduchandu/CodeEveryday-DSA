# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        head=root
        temp=root
        stack=[]
        while temp:
            right_node=temp.right
            temp.right=temp.left
            if right_node!=None:
                stack.append(right_node)
            if temp.right==None:
                if stack:
                    temp.right=stack.pop()
                else:
                    return head
            temp.left=None
            temp=temp.right
            
        
            
