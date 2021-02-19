class Solution:
    def __init__(self):
        self.updated_value = 0

    def convertBST(self, root):
        if root:
            self.convertBST(root.right)
            self.updated_value += root.val
            root.val = self.updated_value
            self.convertBST(root.left)
        return root