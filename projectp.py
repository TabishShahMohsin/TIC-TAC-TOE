import pprint

class Game:
    def __init__(self, game_state):
        self.game_state=game_state
    def __str__(self):
       for i in range(3):
        for j in range(3):
            print(f"| {self.game_state[j+i*3]} ", end="")
        print("|")
        if i!=2:   
            print(" ___"*3+"\n") 


def make_branch(table,move):
    for i in range(9):

        if table[i]=="":
            table_copy=list(table)
            table_copy[i]=move
            # print(table_copy[-1])
            table_copy[-1]=[]
            table[-1].append(table_copy)
            
        
        
def make_tree(working_branch,choice):
    # print(working_branch)
    if choice=="x":
        _choice="o"
    else:
        _choice="x"
    for move in working_branch:
        
        if check_who_won(move)==2:
            make_branch(move,choice)
            make_tree(move[-1],_choice)
        else:
            move[-2]=check_who_won(move)
        

    


def main():

    tree=[""]*10+[[]]
    make_tree([tree],"x")
    pprint.pp(tree)

    
def print_grid(grid):
    # Printing the grid using ASCII, Fomating may not make sense till printed again and again
    for i in range(3):
        for j in range(3):
            print(f"| {grid[j+i*3]} ", end="")
        print("|")
        if i!=2:   
            print(" ___"*3+"\n")

    

        




def check_who_won(l):
    # Checking 3 consecutive horizontally, vertically and diagonally respectively

    if (l[0]==l[1] and l[1]==l[2] and l[2]=="x")| (l[3]==l[4] and l[4]==l[5] and l[5]=="x")|( l[6]==l[7] and l[7]==l[8] and l[8]=="x"):
        return 1 # 1 for win of x
    elif (l[0]==l[3] and l[3]==l[6] and l[6]=="x")|(l[1]==l[4] and l[4]==l[7] and l[7]=="x")|(l[2]==l[5] and l[5]==l[8] and l[8]=="x"):
        return 1
    elif (l[0]==l[4] and l[4]==l[8] and l[8]=="x")|(l[2]==l[4]and l[4]==l[6] and l[6]=="x"):
        return 1
    elif (l[0]==l[1] and l[1]==l[2] and l[2]=="o")|(l[3]==l[4] and l[4]==l[5] and l[5]=="o")|(l[6]==l[7] and l[7]==l[8] and l[8]=="o"):
        return -1 # -1 for win of o
    elif (l[0]==l[3] and l[3]==l[6] and l[6]=="o")|(l[1]==l[4] and l[4]==l[7] and l[7]=="o")|(l[2]==l[5] and l[5]==l[8] and l[8]=="o"):
        return -1
    elif (l[0]==l[4] and l[4]==l[8] and l[8]=="o")|(l[2]==l[4] and l[4]==l[6] and l[6]=="o"):
        return -1
    # Checking if all chances are exhausted: 0 corresponds to draw
    elif l.count("x")+l.count("o")==9:
        return 0
    # If more chances can be played: 2
    else:
        return 2
        




        
def player_move(grid, chance):
    # Preventing the user form entering into a filled block
    while True:
        try:
            inp=int(input(f"Enter from 1 to 9: "))
            inp=inp-1
        except:
            continue
        
        if grid[inp]==" " and chance=="x":
            grid[inp]="x"
            break
        if grid[inp]==" " and chance=="o":
            grid[inp]="o"
            break

if __name__=="__main__":
    main()
    
