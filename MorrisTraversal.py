Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        result = []
        
        while root:
            if root.left:  # There's a left child, need to do some work | Figure out the right most node on the left side of root, and connect it to the root. Why? Because that right-most-guy is the immediate predecessor of the root (Inorder traversal)
                node = root.left
                
                while node.right and node.right!=root:  # There are only two ways where this while loop can break, A) none, or B) You see that there is a loop in your tree! 
                    node = node.right
                    
                if not node.right:   
				    """This is our boy, connect him to root"""
                    node.right = root
                    root = root.left  """Continue to the left branch of the root"""
                else:  """node.right === root | Darn, loop in our tree, remove the connection, deal with root, and proceed to right of root"""
                    result.append(root.val)
                    root = root.right
                
            else:  # no right child, easy peasy, deal with root, and proceed to root's right side
                result.append(root.val)
                root = root.right
                
        return result
