from sys import exit

board = [[]*9]*9
print("Enter the sudoku to be solved row by row:")
s = ""
for i in range(9):
    s = str("line "+str(i+1)+"-> ")
    board[i]=list(map(int,input(s).split()))
sols = 0

def check(i,j,n):
    global board
    l = [board[y][j] for y in range(9)]
    if n not in board[i] and n not in l:
        x0 = (i//3)*3
        y0 = (j//3)*3
        l = [board[x][y] for x in range(x0,x0+3) for y in range(y0,y0+3)]
        if n not in l:
            return True
    return False

def solve():
    global board,sols
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for x in range(1,10):
                    if(check(i,j,x)):
                        board[i][j]=x
                        solve()
                        board[i][j]=0
                return
    sols+=1
    print("Solution",sols,"is ->")
    for item in board:
        print(item)

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            temp = board[i][j]
            board[i][j] = 0
            b = check(i,j,temp)
            board[i][j] = temp
            if not b:
                print("The given board is not a valid sudoku board.")
                exit()
solve()
print("All results printed.")