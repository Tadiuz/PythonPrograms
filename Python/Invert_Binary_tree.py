# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.val)
            self.in_order(root.right)
            
    def invert(self, root: Optional[TreeNode]):
        if not root:
            return
        
        self.invert(root.left)
        self.invert(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.invert(root)
        return(root)

        