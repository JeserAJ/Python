from os import system
from random import randint
from time import sleep
from copy import copy,deepcopy
          
class Gameboard:
    def __init__(self):
        self.board = [["-"]*3,["-"]*3,["-"]*3]

    def printboard(self):
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print("")

    def __check(self):
        #'''0 - game over | 1 - x wins | 2 - o wins'''
        r = 5
        w = ""
        s = self.board
        if s[0][0]==s[0][1] and s[0][1]==s[0][2] and s[0][0]!= "-":
            w = s[0][0]
        elif s[1][0]==s[1][1] and s[1][1]==s[1][2] and s[1][0]!= "-":
            w = s[1][0]
        elif s[2][0]==s[2][1] and s[2][1]==s[2][2] and s[2][0]!= "-":
            w = s[2][0]
        elif s[0][0]==s[1][0] and s[1][0]==s[2][0] and s[0][0]!= "-":
            w = s[0][0]
        elif s[0][1]==s[1][1] and s[1][1]==s[2][1] and s[0][1]!= "-":
            w = s[0][1]
        elif s[0][2]==s[1][2] and s[1][2]==s[2][2] and s[0][2]!= "-":
            w = s[0][2]
        elif s[0][0]==s[1][1] and s[1][1]==s[2][2] and s[0][0]!= "-":
            w = s[0][0]
        elif s[0][2]==s[1][1] and s[1][1]==s[2][0] and s[2][0]!= "-":
            w = s[2][0]
        else :
            for i in s:
                if "-" in i:
                    r = 1
                    break
                r = 0 

        if r == 0:
            return 0
        elif r == 1:
            return 4
        else:
            if w == 'X':
                return 1
            elif w == 'O':
                return 2

    def setpiece(self,P,a,b):
        if self.board[a][b] == "-":
            self.board[a][b] = P
            return self.__check()
        else:
            return 3

    def rempiece(self,a,b):
        self.board[a][b] = "-"

    def check(self):
        return self.__check()

def convert(x):
    if x == 7:
        return [0,0]
    elif x == 8:
        return [0,1]
    elif x == 9:
        return [0,2]
    elif x == 4:
        return [1,0]
    elif x == 5:
        return [1,1]
    elif x == 6:
        return [1,2]
    elif x == 1:
        return [2,0]
    elif x == 2:
        return [2,1]
    elif x == 3:
        return [2,2]

def display(l):
    system("cls")
    print("_____         _____          ")
    print("  |   .   __    |    _    __ " )
    print("  |   |  |__    |   |_|  |__ "  )
    print("\n------------------------------------------")
    print("User your numpad to select location of X\n")
    for i in [[l[0][0],l[0][1],l[0][2],"7","8","9"],[l[1][0],l[1][1],l[1][2],"4","5","6"],[l[2][0],l[2][1],l[2][2],"1","2","3"]]:
        c = 0
        for j in i:
            print(j,end = "  ")
            c+=1
            if c == 3:
                print("\t", end="")
        print("\n")
    
def check(c):
    if con == 0:
        print("Game over. Nobody wins\n")
        return False
    elif con == 1:
        print("Congrats! You won :)\n")
        return False
    elif con == 2:
        print("The computer wins. ^-^\n")
        return False
    else:
        return True

def compch(g):
    x = convert(randint(1,9))
    if g[x[0]][x[1]]=="-":
        return x
    else:
        return compch(g)

def minmax(g,pos,player):
    t = g.check()
    if t==0:
        return 0,0
    elif t == 1:
        return -10,0
    elif t == 2:
        return 10,0

    g2 = deepcopy(g)
    moves = []
    for i in pos:
        p = copy(pos)
        m = {}
        x = convert(i)
        p.remove(i)
        if player == "O":
            g2.setpiece('O',x[0],x[1])
            mm = minmax(g2,p,"X")
        else:
            g2.setpiece('X',x[0],x[1])
            mm = minmax(g2,p,"O")
        g2.rempiece(x[0],x[1])
        m["pos"] = i
        m["score"] = mm[0]
        moves.append(m)

    p = 0
    if player == "O":
        bst = -11
        for i in moves:
            if i["score"]>bst:
                bst = i["score"]
                p = i["pos"]
    else:
        bst = 11
        for i in moves:
            if i["score"]<bst:
                bst = i["score"]
                p = i["pos"]

    return bst,p

if __name__ == "__main__":
    g = Gameboard()
    display(g.board)
    pos = [i for i in range(1,10)]
    play = True
    while play:
        print("\n Your Choice -> ")
        y = int(input())
        x = convert(y)
        con = g.setpiece('X',x[0],x[1])
        while con == 3:
            y = int(input("Please enter a free cell ->"))
            x = convert(y)
            con = g.setpiece('X',x[0],x[1])
        pos.remove(y)   
        display(g.board)

        play = check(con)
        if not play:
            break
        print("Computer's turn ......")
        sleep(1)

        #x = compch(g.board)
        y = minmax(g,pos,'O')[1]
        x = convert(y)
        con = g.setpiece('O',x[0],x[1])
        pos.remove(y)
        display(g.board)
        play = check(con)
