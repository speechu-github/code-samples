class Board():
    def __init__(self, board):
        self.board = board

    def addToken(self, row, col, token):
        if self.board[row][col] == 'O' or self.board[row][col] == 'X':
            return "Unavailable"

        self.board[row][col] = token
        for row in range(n):
            Xcount = 0
            for col in range(n):
                if self.board[row][col] == 'X':
                    Xcount+=1
            if Xcount == n: 
                return "Won"

        for col in range(n):
            Xcount = 0
            for row in range(n):
                if self.board[row][col] == 'X':
                    Xcount+=1
            if Xcount == n: 
                return "Won"

        Xcount = 0
        for i in range(n):
            if self.board[i][i] == 'X':
                Xcount+=1
            if Xcount == n:
                return "Won"

        Xcount = 0
        for i in range(n):
            if self.board[i][n-1-i] == 'X':
                Xcount+=1
            if Xcount == n:
                return "Won"

        return "None"
   
    def printBoard(self):
        for row in range(n):
            for col in range(n):
                print(self.board[row][col], end="")
                if col != n-1:
                    print("|",end="")
                else:
                    print("")

   
    def isFull(self):
        for row in range(n):
            for col in range(n): 
                if self.board[row][col] == '-':
                    return False

        return True

    def winOrBlock(self, checkToken, checkCount, fillToken):
        for row in range(n):
            CompCount=0
            EmptyCount=0
            for col in range(n):
                if self.board[row][col] == checkToken:
                   CompCount+=1 
                if self.board[row][col] == '-':
                   EmptyCount+=1 
            if CompCount == checkCount and EmptyCount == n-checkCount:
                for col in range(n):
                    if self.board[row][col] == '-':
                        self.board[row][col] = fillToken 
                        return True

        for col in range(n):
            CompCount=0
            EmptyCount=0
            for row in range(n):
                if self.board[row][col] == checkToken:
                   CompCount+=1 
                if self.board[row][col] == '-':
                   EmptyCount+=1
            if CompCount == checkCount and EmptyCount == n-checkCount:
                for row in range(n):
                    if self.board[row][col] == '-':
                        self.board[row][col] = fillToken 
                        return True

        CompCount=0
        EmptyCount=0
        for i in range(n):
            if self.board[i][i] == checkToken:
                CompCount+=1
            if self.board[i][i] == '-':
                EmptyCount+=1
            if CompCount == checkCount and EmptyCount == n-checkCount:
                for i in range(n):
                    if self.board[i][i] == '-':
                       self.board[i][i] = fillToken 
                       return True

        CompCount=0
        EmptyCount=0
        for i in range(n):
            if self.board[i][n-1-i] == checkToken:
                CompCount+=1
            if self.board[i][n-1-i] == '-':
                EmptyCount+=1
            if CompCount == checkCount and EmptyCount == n-checkCount:
                for i in range(n):
                    if self.board[i][n-1-i] == '-':
                       self.board[i][n-1-i] = fillToken 
                       return True

        return False

    def makeMove(self):
        # Can I win? Go for it
        ret = self.winOrBlock('O', n-1, 'O')
        if ret == True:
            return "Won" 
 
        # Should I block? Go for it
        ret = self.winOrBlock('X', n-1, 'O')
        if ret == True:
            return "Blocked"

        # Set up for a win 
        ret = self.winOrBlock('O', n-2, 'O')
        if ret == True:
            return "FilledForWin"

        # Fill the center if you can
        for row in range(1,n-1):
            for col in range(1,n-1):
                if self.board[row][col] == '-':
                    self.board[row][col] = 'O'
                    return "FilledCenter"

        # Find an empty row or column and fill it.
        for row in range(n):
            EmptyCount=0;
            for col in range(n):
                if self.board[row][col] == '-':
                    EmptyCount+=1
            if EmptyCount == n:
                self.board[row][0] = 'O'
                return "Filled"

        for col in range(n):
            EmptyCount=0;
            for row in range(n):
                if self.board[row][col] == '-':
                    EmptyCount+=1
            if EmptyCount == n:
                self.board[0][col] = 'O'
                return "Filled"

        # Find an empty spot and fill it.
        for row in range(n):
            for col in range(n):
                if self.board[row][col] == '-':
                    self.board[row][col] = 'O'
                    return "Filled"

        return "None"

#Initialize Board
board = []
while True:
    n = input("Enter grid size (eg, enter '3' for 3x3 grid): ")
    n = int(n)
    if n < 3:
        print("Size too small, pick size of 3 or more")
        continue
    break
 
for row in range(n):
    row = []
    for col in range(n):
        row.append('-')
    board.append(row)

b = Board(board);
b.printBoard()
print()

#Play game interactively
win = False
while b.isFull() == False:
    row, col = input("Enter row, column values (eg. 1 2): ").split() 
    row = int(row) - 1
    col = int(col) - 1
    if row < 0 or row >= n:
        print("Invalid row value")
        continue
    if col < 0 or col >= n:
        print("Invalid column value")
        continue

    action = b.addToken(row, col, 'X')
    if action == "Unavailable":
        print("Unavailable, pick different row, column values")
        continue
    
    b.printBoard()
    if action == "Won":
        print("You won!")
        win = True
        break
    action = b.makeMove()
    print("Computer made a move")
    b.printBoard()
    if action == "Won":
        print("The Computer won!")
        win = True
        break

if win != True:
    print("It's a tie!")
