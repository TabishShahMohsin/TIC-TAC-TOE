import random
import os
import json

def move(state):
    for i in range(3):
        try:
            if state["chance"]=="o":
                recommended_move=random.choice(state["children"][i])
            else:
                recommended_move=random.choice(state["children"][2-i])
        except IndexError:
            pass
        else:
            break
    return recommended_move
        
        
        

    



def main():

    with open("All_Games.json") as file_handler:
        tree=json.load(file_handler)
    
    # Clearing the terminal before start
    os.system("cls" if os.name == "nt" else "clear")
    
    
    # Just to show the user the grid marking
    printing_grid=[]
    for i in range(3):
        for j in range(3):
             printing_grid.append(i*3+j+1)
    Print(printing_grid)
    
    print("\nWelcome to TicTacToe!")
    
    
    
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
            next_move=move(next_move)
            #Printing the grid to the user again and again
            # next_move.Print()
            Print(next_move["state"])
    
            if next_move["status"]!=2:
                break
        
        # Player move:
        player=player_move(list(next_move["state"]),choice)
        for i in next_move["children"]:
            for j in i:
                if player==j["state"]:
                    next_move=j
          
        os.system("cls" if os.name == "nt" else "clear")

        # Ending the game if win/lose/draw
        if next_move["status"]!=2:
            break
          
          
            
        if choice=="x":
        # Storing the optimal move for o in l
            next_move=move(next_move)
        
        #Printing the grid to the user again and again
            # next_move.Print()
            Print(next_move["state"])
            # Ending the game if win/lose/draw
            if next_move['status']!=2:
                break 
        
    # The player will never win, In Sha ALLAH 
    # next_move.Print()
    if next_move["status"]!=0:
        print("Computer Wins!!")
    else:
        print("It's Draw!, you'll never win against me!")
    # next_move.Print()
    Print(next_move["state"])


        
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