board = [
    [2, 0, 0, 2], 
    [4, 16, 8, 2], 
    [2, 64, 32, 4], 
    [1024, 1024, 64, 0]]

def left():
    for row in board:
        zeros = len([*filter(lambda x: not x, row)])
        row[:] = list([*filter(lambda x: x,row)] + [0]*zeros)
        for i in range(3-zeros):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0
                left()

def right():
    for row in board:
        zeros = len([*filter(lambda x: not x, row)])
        row[:] = list([0]*zeros + [*filter(lambda x: x,row)])
        for i in range(3, zeros, -1):
            if row[i] == row[i-1]:
                row[i] *= 2
                row[i-1] = 0
                right()



            



# match input():
#     case "0":
#         left()
#     case "1":
#         up(),
#     case "2":
#         right(),
#     case "3":
#         down(),
up()
print(board)
