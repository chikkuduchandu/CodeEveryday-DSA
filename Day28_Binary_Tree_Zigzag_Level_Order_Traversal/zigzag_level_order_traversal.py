

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return res
        s1=[]
        s1.append(root)
        s2=[]
        st=True
        while s1 or  s2:
            tp=[]
            if st:
                while  s1:
                    nn = s1.pop()
                    tp.append(nn.val)
                    if(nn.left):
                        s2.append(nn.left)
                    if(nn.right):
                        s2.append(nn.right)
                st=False
            else:
                while s2:
                    nn = s2.pop()
                    tp.append(nn.val)
                    if(nn.right):
                        s1.append(nn.right)
                    if(nn.left):
                        s1.append(nn.left)
                st=True
            res.append(tp)
        return res
        
        



        
