class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize the dictionary to store the nodes at each vertical level
        self.dictt = {}
        # Call the vertical function to populate the dictionary with nodes and their coordinates
        self.vertical(root, 0, 0)
        # Sort the keys of the dictionary (i.e. the vertical levels) in ascending order
        temp = sorted(self.dictt)
        # Initialize the result list
        res = []
        # Iterate through the sorted keys of the dictionary
        for ind in temp:
            # Get the nodes at the current vertical level
            self.dictt[ind].sort()
            tmp = []
            # Iterate through the sorted nodes and append their values to the temporary list
            for nod in self.dictt[ind]:
                tmp.append(nod[1])
            # Append the temporary list to the result list
            res.append(tmp)
        # Return the final result
        return res

    def vertical(self, node, x, y):
        # If the node is None, return
        if not node:
            return 
        # If the current vertical level already exists in the dictionary, append the node to the list of nodes at that level
        if y in self.dictt:
            self.dictt[y].append((x, node.val))
        # Otherwise, add a new key-value pair to the dictionary with the current vertical level and a list containing the current node
        else:
            self.dictt[y] = [(x, node.val)]
        # Recursively call the vertical function for the left and right children of the current node, adjusting the x and y coordinates accordingly
        self.vertical(node.left, x + 1, y - 1)
        self.vertical(node.right, x + 1, y + 1)