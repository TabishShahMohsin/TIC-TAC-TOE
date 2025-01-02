import random
import os


class Board:
    def __init__(self, game_state, chance):
        self.chance=chance
        self.state=game_state
        self.children=[]
        self.make_branch(chance)
        self.status=self.check_who_won()
        self.value=self.get_minimax()
        self.min=-1
        self.max=1
        self.children=self.sort()
        
     
                
                
    def check_who_won(self):
            
                # Checking 3 consecutive horizontally, vertically and diagonally respectively
            for i in range(3):
                if self.state[0+3*i]==self.state[1+3*i]==self.state[2+3*i]:
                    if self.state[0+3*i]=="x":
                        return 1
                    elif self.state[0+3*i]=="o":
                        return -1
                elif self.state[0+i]==self.state[3+i]==self.state[6+i]:
                    if self.state[0+i]=="x":
                        return 1
                    elif self.state[0+i]=="o":
                        return -1

            for i in range(2):
                if self.state[6*i]==self.state[4]==self.state[-6*i+8]:
                    if self.state[6*i]=="x":
                        return 1
                    elif self.state[6*i]=="o":
                        return -1
            # Checking if all chances are exhausted: 0 corresponds to draw
            if self.state.count("x")+self.state.count("o")==9:
                return 0
                
            # If more chances can be played: 2
            return 2
    

    def make_branch(self,move):
        _chance="x" if self.chance=="o" else "o"
        for i in range(9):

            if self.state[i]==" ":
                branch_copy=list(self.state)
                branch_copy[i]=move
                self.children.append(Board(branch_copy, _chance))
                
                
                
    def get_minimax(self):
        values=[]
        if self.status!=2:
            return self.status
        for i in self.children:
            values.append(i.value)
        self.min=min(values)
        self.max=max(values)
        if self.chance=="x":
            return self.max
        else:
            return self.min
        
        
    def sort(self):
        sorted_children=[[],[],[]]
        for i in self.children:
            sorted_children[i.value+1].append(i)
        return sorted_children        
    
    
    def move(self):
        for i in range(3):
            try:
                if self.chance=="o":
                    recommended_move=random.choice(self.children[i])
                else:
                    recommended_move=random.choice(self.children[2-i])
            except IndexError:
                pass
            else:
                break
        return recommended_move
            
        
        

    



def main():
    
    # Clearing the terminal before start
    os.system("cls" if os.name == "nt" else "clear")
    
    
    # Just to show the user the grid marking
    printing_grid=[]
    for i in range(3):
        for j in range(3):
             printing_grid.append(i*3+j+1)
    Print(printing_grid)
    
    print("\nWelcome to TicTacToe!")
   




    tree=Board([" ", " ", " ", " ", " ", " ", " ", " ", " "],"x")
    
    
    # Asking the user to choose for x or o
    while True:
        choice=input("Would you like to play enter x or o: ")
        if choice in ["x", "o"]:
            break
    
    game_moves=[] 
    
    game_moves.append(tree)
 
    # Performing the actual grid loop till the game ends, (game-loop)
        # CLearing the window before every play
   
    # Performing the actual grid loop till the game ends, (game-loop)
    if choice=="o":
        game_moves.append(game_moves[-1].move())
        Print(game_moves[-1].state)
    while True:
    # Player move:
        player=player_move(list(game_moves[-1].state),choice)
        if player not in ["undo","redo"]:
            for i in game_moves[-1].children:
                for j in i:
                    if player==j.state:

                        game_moves.append(j) 
            _game_moves=list(game_moves)
        elif player=="undo":
            if len(game_moves)>1:
                game_moves=game_moves[:-2]
                os.system("cls" if os.name == "nt" else "clear")
                Print(game_moves[-1].state)
            else:
                print("Nothing to undo.")
            continue

        elif player=="redo":
            if len(game_moves)<len(_game_moves):
                game_moves=_game_moves[:len(game_moves)+2]
                os.system("cls" if os.name == "nt" else "clear")
                Print(game_moves[-1].state)
            else:
                print("Nothing to redo.")
            continue
        if game_moves[-1].status!=2:
            break
        os.system("cls" if os.name == "nt" else "clear")
        c=game_moves[-1].move()
        game_moves.append(c)
        _game_moves.append(c)

        if game_moves[-1].status!=2:
            break
        Print(game_moves[-1].state)

       
    # The player will never win, In Sha ALLAH 
    # next_move.Print()
    if game_moves[-1].status!=0:
        print("Computer Wins!!")
    else:
        print("It's Draw!, you'll never win against me!")
    # next_move.Print()
    Print(game_moves[-1].state)


        
# Making a printing funciton:
def Print(table):
    for i in range(3):
        for j in range(3):
            print(f"| {table[j+i*3]} ", end="")
        print("|")
        if i!=2:   
            print(" ___"*3+"\n")







        
def player_move(grid, chance):
    # Preventing the user form entering into a filled block
    while True:
        
        inp=(input(f"Enter from 1 to 9: "))
        try:
            inp=int(inp)-1
        except ValueError:
            if inp.lower().strip()=="undo":
                return "undo"
            elif inp.lower().strip()=="redo":
                return "redo"
            continue
        
        if grid[inp]==" " and chance=="x":
            grid[inp]="x"
            break
        if grid[inp]==" " and chance=="o":
            grid[inp]="o"
            break
    return grid
        
        

if __name__=="__main__":
    main()
