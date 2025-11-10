# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findPath(self,node,target,path):
        
        if node==None:
            return []
        if node.val==target.val:
            path.append(target)
            return path
        return self.findPath(node.left,target,path+[node])+self.findPath(node.right,target,path+[node])
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        path1=self.findPath(root,p,[])
        
        path2=self.findPath(root,q,[])

        ans=path1[0]
        i=0
        while i<len(path1) and i<len(path2) and path1[i]==path2[i]:
            ans=path1[i]
            i+=1
        return ans 
        
        
