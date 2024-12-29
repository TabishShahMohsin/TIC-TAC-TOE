import random
import os


class Game:
    def __init__(self, game_state, chance):
        self.chance=chance
        self.state=game_state
        self.children=[]
        self.make_branch(chance)
        self.status=self.check_who_won()
        self.value=self.get_minimax()
        self.min=-1
        self.max=1
        
        
    def Print(self):
        for i in range(3):
            for j in range(3):
                print(f"| {self.state[j+i*3]} ", end="")
            print("|")
            if i!=2:   
                print(" ___"*3+"\n") 
                
                
    def check_who_won(self):
            
                # Checking 3 consecutive horizontally, vertically and diagonally respectively
            for i in range(3):
                if self.state[0+3*i]==self.state[1+3*i]==self.state[2+3*i]:
                    return 1  if self.state[0+3*i]=="x" else -1
                elif self.state[0+i]==self.state[3+i]==self.state[6+i]:
                    return 1  if self.state[0+i]=="x" else -1
            for i in range(2):
                if self.state[6*i]==self.state[4]==self.state[-6*i+8]:
                    return 1  if self.state[8*i]=="x" else -1
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
                self.children.append(Game(branch_copy, _chance))
                
                
                
    def get_minimax(self):
        values=[]
        if self.status!=2:
            return self.status
        for i in self.children:
            values.append(i.value)
        if self.chance=="x":
            return max(values)
        else:
            return min(values)
                
            
        
        

    



def main():
    
    os.system("cls" if os.name == "nt" else "clear")
    
    # Just to show the user the grid marking
    printing_grid=[]
    for i in range(3):
        for j in range(3):
            printing_grid.append(i*3+j+1)

    Game(printing_grid).Print
    
    print("\nWelcome to TicTacToe!")
    
    
    # Asking the user to choose between x and o
    while True:
        choice=input("Would you like to play enter x or o: ")
        if choice in ["x", "o"]:
            break
    
    
    
    # Performing the actual grid loop till the game ends, (game-loop)
    while True:
        if choice=="o":
            # Getting the best move for x
            
            grid=max_ll(minimax(grid, grid_width, winning_length))
            #Printing the grid to the user again and again
            print_grid(grid)
            
            state=check_who_won(grid, grid_width, winning_length)
            if state!=2:
                break
        
        
        if player_move(choice,grid, grid_width)=="undo":
            grid=prev_grid
        else:
            prev_grid=list(grid)
        os.system("cls" if os.name == "nt" else "clear")
        
          
          
        # Ending the game if win/lose/draw
        state=check_who_won(grid, grid_width, winning_length)
        if state!=2:
            break
          
          
            
        if choice=="x":
        # Storing the optimal move for o in l
            grid=min_ll(minimax(grid, grid_width, winning_length))
        
        #Printing the grid to the user again and again
            print_grid(grid)
            # Ending the game if win/lose/draw
            state=check_who_won(grid, grid_width, winning_length)
            if state!=2:
                break 
        
    # The player will never win, In Sha ALLAH 
    if state!=0:
        print("Computer Wins!!")
    else:
        print("It's Draw!, you'll never win against me!")
    print(grid)


        









        
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
    
