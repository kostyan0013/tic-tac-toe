from random import choice

"""def check_turn(f,f1):
    if (f == f1) or (levenshtein(f,f1) > 1) or (len(f)<9) or (len(f) > 9):
        return False
        exit
    for i in range(0,10):
        if (f1[i] != f[i]) and (f[i] != 0):
            return False
            exit
    else:
        return True"""

def levenshtein(k,p): 
    mx = 0
    for i in range(len(k)):
        if k[i] != p[i]:
            mx += 1
    return mx

def check_win(s):
    for i in range(3):
        if s[3*i] == s[3*i+1] == s[3*i+2] != -1:
            if s[3*i] == 0:
                print 'O\'s wins \n'
                return True,
            else:
                print 'X\'s wins\n'
                return True
            exit
        if s[i] == s[i+3] == s[i+6] != -1:
            if s[i] == 0:
                print 'O\'s wins \n'
                return True,
            else:
                print 'X\'s wins\n'
                return True
            exit
    if ((s[0] == s[4] == s[8]) or (s[2] == s[4] == s[6]))and(s[4] != -1):
        if s[4] == 0:
            print 'O\'s wins \n'
            return True
        else:
            print 'X\'s wins\n'
            return True
        exit
    for i in range(9):
        if s[i] == -1:
            return False
            exit
    print 'Draw'
    return True
    
def print_board(board):
    for i in range(3):
        print " ",
        for j in range(3):
            if board[i*3+j] == 1:
                print 'X',
            elif board[i*3+j] == 0:
                print 'O',
            elif board[i*3+j] == -1:
                print i*3+j+1,  

            else:
                print ' ',
            
            if j != 2:
                print " | ",
        print
        
        if i != 2:
            print "-----------------"
        else: 
            print

def fill(s,k,turn):
    if ((s[k[0]] == s[k[1]] == turn % 2) and (s[k[2]] == -1)): return k[2]
    elif ((s[k[0]] == s[k[2]] == turn % 2) and (s[k[1]] == -1)): return k[1]
    elif ((s[k[1]] == s[k[2]] == turn % 2) and (s[k[0]] == -1)): return k[0]

def take_side(s):
    for x in [1,3,5,7]:
        if s[x] == -1: return x
        
def take_corner(s):
    for x in [0,2,6,8]:
        if s[x] == -1: return x
        
def bot_turn(s,turn):
    for i in range(3):
        if (fill(s,[i,i+3,i+6],turn) != None): return fill(s,[i,i+3,i+6],turn)
        elif (fill(s,[3*i,3*i+1,3*i+2],turn) != None): return fill(s,[3*i,3*i+1,3*i+2],turn)
    if (fill(s,[0,4,8],turn) != None): return fill(s,[0,4,8],turn)
    elif fill(s,[2,4,6],turn): return fill(s,[2,4,6],turn)

    for i in range(3):
        if (fill(s,[i,i+3,i+6],turn+1) != None): return fill(s,[i,i+3,i+6],turn+1)
        elif (fill(s,[3*i,3*i+1,3*i+2],turn+1) != None): return fill(s,[3*i,3*i+1,3*i+2],turn+1)
    if (fill(s,[0,4,8],turn+1) != None): return fill(s,[0,4,8],turn+1)
    elif fill(s,[2,4,6],turn+1): return fill(s,[2,4,6],turn+1)
    
    if s[4] == -1: return 4
    if turn % 2 == 1:
        if (s[0] == 0) and (s[8] == -1): return 8
        if (s[1] == 0) and ((s[8] == -1) or s[6] == -1):
            return 6 if s[6] == -1 else 8
        if (s[2] == 0) and (s[6] == -1):
            return 6
        if (s[5] == 0) and ((s[0] == -1) or s[6] == -1):
            return 0 if s[0] == -1 else 6
        if (s[8] == 0) and (s[0] == -1): return 0
        if (s[7] == 0) and ((s[0] == -1) or s[2] == -1):
            return 0 if s[0] == -1 else 2
        if (s[6] == 0) and (s[2] == -1): return 2
        if (s[3] == 0) and ((s[2] == -1) or s[8] == -1):
            return 2 if s[2] == -1 else 8
    if turn % 2 == 0:
        if s[4] == 1:
            if (take_corner(s) != None): return take_corner(s)
            else: return take_side(s)
        elif ((s[0] == 1) or (s[2] == 1) or (s[6] == 1) or (s[8] == 1)):
            if turn == 4:
                if (take_corner(s) != None): return take_corner(s)
                else: return take_side(s)
            else: return take_side(s)
        else:
            if (take_corner(s) != None): return take_corner(s)        
            
    return take_side(s)
    
    
def play_bot(mode):
    board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    turn = 1
    if mode == '1':
        while not(check_win(board)):
            print_board(board)
            while True:
                try:
                    current = raw_input('Choose place for %s' % ('X: ' if turn%2 == 1 else 'O: '))
                    current = int(current)-1
                except ValueError:
                    print 'Wrong turn'
                else:
                    if try_turn(board,turn,current): break
            if check_win(board): break
            turn += 1
            try_turn(board,turn,bot_turn(board,turn))
            turn += 1
    elif mode == '0':
        while not(check_win(board)):
            try_turn(board,turn,bot_turn(board,turn))
            print_board(board)
            turn += 1
            if check_win(board): break
            while True:
                try:
                    current = raw_input('Choose place for %s' % ('X: ' if turn%2 == 1 else 'O: '))
                    current = int(current)-1
                except ValueError:
                    print 'Wrong turn'
                else:
                    if try_turn(board,turn,current): break
            turn += 1
    print_board(board)

def try_turn(board,turn,current):
    if (0<=current<9)and(board[current] == -1):
        board[current] = turn % 2
        return True
    else:
        print 'Wrong turn'
    
def play_gamers():
    board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    turn = 1
    while not(check_win(board)):
        print_board(board)
        current = raw_input('Choose place for %s' % ('X: ' if turn%2 == 1 else 'O: '))
        try:
            current = int(current)-1
            try_turn(board,turn,current)
        except:
            print 'Wrong turn'
        turn += 1
    print_board(board)
    
while True:
    mode = raw_input("Write 1 to play for X or 0 for O: ")
    play_bot(mode)
