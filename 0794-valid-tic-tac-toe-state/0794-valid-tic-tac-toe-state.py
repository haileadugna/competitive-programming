class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        row, col = len(board), len(board[0])
        xCount, oCount = 0, 0
        
        def checkStatusWinner(board, ans):
            self.ans = ans
            status = ''

            if board[0][2] == board[1][1] == board[2][0] !=' ':
                status = board[0][2]
                self.ans.append(board[0][2])
            if board[0][0] == board[1][1] == board[2][2] !=' ':
                self.ans.append(board[0][0])
                status = board[0][0]
            if board[0][0] == board[0][1] == board[0][2] !=' ':
                self.ans.append(board[0][0])
                status = board[0][0]
            if board[0][2] == board[1][2] == board[2][2] !=' ':
                self.ans.append(board[1][2])
                status = board[0][2]
            if board[2][2] == board[2][1] == board[2][0] !=' ':
                self.ans.append(board[2][2])
                status = board[2][2]
            if board[2][0] == board[1][0] == board[0][0] !=' ':
                self.ans.append(board[2][0])
                status = board[2][0]
            if board[0][1] == board[1][1] == board[2][1] !=' ':
                self.ans.append(board[0][2])
                status = board[0][1]
            if board[1][0] == board[1][1] == board[1][2] !=' ':
                self.ans.append(board[1][1])
                status = board[1][1]
            res = [status, self.ans]
            return res

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    xCount += 1
                elif board[i][j] == 'O':
                    oCount += 1

        if xCount < oCount or oCount+1 < xCount :
            return False

        res = checkStatusWinner(board, [])
        status = res[0]
        ans = res[1]
        # print(ans)
        if len(set(ans)) > 1:
            return False
        
        if status == 'X':
            return xCount == oCount+1
        if status == 'O':
            return xCount == oCount
        
        return True