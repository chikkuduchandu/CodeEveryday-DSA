from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        q=deque()
        q.append(root)
        ans=[]
        while q:
            curr_list=[]
            l=len(q)
            for i in range(l):
                node=q.popleft()
                curr_list.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            ans.append(curr_list)
        return ans
