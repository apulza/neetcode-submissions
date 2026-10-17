# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively find the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update the global maximum diameter if the path through 
            # the current node is longer than any path found so far
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the maximum depth/height of the current subtree to its parent
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.max_diameter
