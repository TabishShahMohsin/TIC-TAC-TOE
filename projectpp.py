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
                self.children.append(Game(branch_copy, _chance))
                
                
                
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
    
    tree=Game([" ", " ", " ", " ", " ", " ", " ", " ", " "],"x")
    
    
    # Asking the user to choose for x or o
    while True:
        choice=input("Would you like to play enter x or o: ")
        if choice in ["x", "o"]:
            break
    
    
    next_move=tree
    
    
    # Performing the actual grid loop till the game ends, (game-loop)
    while True:
        # CLearing the window before every play
        
        
        if choice=="o":
            # Getting the best move for x
            next_move=next_move.move()
            #Printing the grid to the user again and again
            # next_move.Print()
            Print(next_move.state)
    
            if next_move.status!=2:
                break
        
        # Player move:
        player=player_move(list(next_move.state),choice)
        for i in next_move.children:
            for j in i:
                if player==j.state:
                    next_move=j
          
        os.system("cls" if os.name == "nt" else "clear")

        # Ending the game if win/lose/draw
        if next_move.status!=2:
            break
          
          
            
        if choice=="x":
        # Storing the optimal move for o in l
            next_move=next_move.move()
        
        #Printing the grid to the user again and again
            # next_move.Print()
            Print(next_move.state)
            # Ending the game if win/lose/draw
            if next_move.status!=2:
                break 
        
    # The player will never win, In Sha ALLAH 
    # next_move.Print()
    if next_move.status!=0:
        print("Computer Wins!!")
    else:
        print("It's Draw!, you'll never win against me!")
    # next_move.Print()
    Print(next_move.state)


        
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
        try:
            inp=int(input(f"Enter from 1 to 9: "))
            inp=inp-1
        except ValueError:
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