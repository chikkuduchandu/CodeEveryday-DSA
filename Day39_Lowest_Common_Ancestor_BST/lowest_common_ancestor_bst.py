# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findAncestor(self,node,p,q):
        
        if p.val<node.val and q.val>node.val:
            return node
        if p.val==node.val:
            return p
        elif q.val==node.val:
            return q
        if p.val<node.val and q.val<node.val:
            return self.findAncestor(node.left,p,q)
        elif p.val>node.val and q.val>node.val:
            return self.findAncestor(node.right,p,q)
        
        

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if p.val<q.val:
            return self.findAncestor(root,p,q)
        else:
            return self.findAncestor(root,q,p)

        
        
