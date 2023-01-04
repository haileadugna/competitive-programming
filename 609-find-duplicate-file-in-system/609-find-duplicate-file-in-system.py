class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # res = []
        # n = len(paths)
        # dictt = defaultdict(list)
        # for word in paths:
        #     temp = word.split(" ")
        #     m = len(temp)
        #     for  i in range(1, m):
        #         temp1 = temp[i].split("(")
        #         dictt[temp1[-1]].append(temp[0] + "/" + temp1[0])
        # for key, item in dictt.items():
        #     if len(list(item)) > 1:
        #         res.append(item)
        # return res
        files = {}
        for path in paths:
            # Split the path into the directory and the file descriptions
            parts = path.split(" ")
            dir = parts[0]
            # Iterate through the file descriptions
            for i in range(1, len(parts)):
                # Split the file description into the file name and content
                file_parts = parts[i].split("(")
                file_name = file_parts[0]
                content = file_parts[1][:-1]
                # Add the file to the hash map
                if content not in files:
                    files[content] = []
                files[content].append(dir + "/" + file_name)
        # Create the final output by filtering out any entries with only one file
        output = []
        for k, v in files.items():
            if len(v) > 1:
                output.append(v)
        return output