class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)-1):
            if command[i] == "G" :
                ans += "G"
            elif command[i] == "(" and command[i+1] == ")":
                ans += "o"
            elif command[i] == "a" or command[i] == "l" or command[i] == ")":
                continue
            else:
                ans += "al"
        if command[-1] == "G":
            ans += "G"
        return ans