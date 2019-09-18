# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        queue = [root]
        res = []

        while queue:
            res.append(sum([node.val for node in queue]) * 1.0 / len(queue))

            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            queue = temp

        return res

        # T:O(n) - # of nodes in the tree
        # S: O(m) - max num of nodes in one level
