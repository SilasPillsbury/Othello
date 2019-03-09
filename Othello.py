b =[[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]

def play(b):
    'Things'
    return None

def check_playable(player,location,board):
    """
    Player - int 1 or 2, location - length 2 index,
    board - current board state, has nested indexes
    """
    playable = False
    
    if b[location[0]][location[1]] != 0:
        return playable
        #performs check if spot is empty
    
    for x in board[location[0]][location[1]+1:8]:
        if x == abs(3-player):
            playable = True
            continue
        if x == 0:
            playable = False
            break
        if x == player:
            break

    if playable:
        return playable
    
    for entry in range(8-location[1]):
        y = board[entry][location[1]]

    
