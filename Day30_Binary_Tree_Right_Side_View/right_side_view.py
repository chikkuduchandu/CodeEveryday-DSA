from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root==None:
            return []
        q=deque()
        ans=[]
        ans.append(root.val)
        q.append(root)
        while q:
            l=len(q)
            curr_list=[]
            for i in range(l):
                node=q.popleft()
                if node.left!=None:
                    curr_list.append(node.left.val)
                    q.append(node.left)
                if node.right!=None:
                    curr_list.append(node.right.val)
                    q.append(node.right)
            if curr_list:
                ans.append(curr_list[-1])
        return ans

        
