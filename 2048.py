board = [[*map(int,input().split())] for _ in range(4)]

def left():
    for row in board:
        frow = [*filter(bool,row)]
        for i in range(len(frow)-1):
            if frow[i] == frow[i+1]:
                frow[i] *= 2
                frow[i+1] = 0
        frow = [*filter(bool,frow)]
        row[:] = frow + [0]*(4-len(frow))
            
def right():
    for row in board:
        frow = [*filter(bool,row)]
        for i in range(len(frow)-1,0,-1):
            if frow[i] == frow[i-1]:
                frow[i] *= 2
                frow[i-1] = 0
        frow = [*filter(bool,frow)]
        row[:] = [0]*(4-len(frow)) + frow
    
def up():
    for col in range(4):
        fcol = [*filter(bool,[row[col] for row in board])]
        for i in range(len(fcol)-1):
            if fcol[i] == fcol[i+1]:
                fcol[i] *= 2
                fcol[i+1] = 0
        fcol = [*filter(bool,fcol)]
        fcol = fcol + (4-len(fcol))*[0]
        for row in range(4):
            board[row][col] = fcol[row]   

def down():
    for col in range(4):
        fcol = [*filter(bool,[row[col] for row in board])]
        for i in range(len(fcol)-1,0,-1):
            if fcol[i] == fcol[i-1]:
                fcol[i] *= 2
                fcol[i-1] = 0
        fcol = [*filter(bool,fcol)]
        fcol = (4-len(fcol))*[0] + fcol
        for row in range(4):
            board[row][col] = fcol[row]

{
    "0": left,
    "1": up,
    "2": right,
    "3": down
}[input()]()

for row in board:
    print(*row)
