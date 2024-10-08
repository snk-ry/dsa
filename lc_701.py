""" Leetcode 701

    Insert into a binary search tree
    https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""

# Definition for a binary tree node.
# class Node:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root, val):

        if not root:
            return Node(val)

        if root:
            
            temp = root
            
            while temp:
            
                if val > temp.val:
                    
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = Node(val)
                        break
                
                elif val < temp.val:

                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = Node(val)
                        break
        
        return root