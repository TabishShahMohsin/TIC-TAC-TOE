def main():
    
    # Asking the user to choose between x and o
    choice=input("Welcome to TicTacToe! \nEnter x or o: ")
    
    # Just to show the user the grid marking
    l=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print_grid(l)
    
    # The default grid with extra element for value (len(l))=10 and not 9
    l=[" ", " ", " ", " ", " ", " ", " ", " ", " "," "]
    
    # Performing the actual grid loop till the game ends
    while True:
        
        # Ending the game if win/lose/draw
        c=check_who_won(l)
        if c!=2:
            break
        
        #Preventing the user form entering into a filled block
        while True:
            x=int(input("Enter from 1 to 9: "))-1
            if l[x]==" ":
                l[x]="x"
                break
          
        # Ending the game if win/lose/draw
        c=check_who_won(l)
        if c!=2:
            break  
          
            
        
        # Storing the optimal move for o in l
        l=min_ll(minimax(l))
        
        #Printing the grid to the user again and again
        print_grid(l)
        
    if c==1:
        print("X has won.")
    elif c==-1:
        print("O has won.")
    elif c==0:
        print("It's Draw!, you can't win against computer!")
    
    
def print_grid(l):
    # Printing the grid using ASCII, Fomating may not make sense till printed again and again
    k=0
    for i in range(3):
        for j in range(3):
            print(f"| {l[k]} ", end="")
            k=k+1
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
        
        

# Try to construct a minimax
def minimax(l):
    
    # d should store the choices for the one move after l and their values as the last element of l
    d=[]
    
    # A new move after l was achieved
    for i in range(len(l)-1):
        
        # Move has to be played at an empty spot
        if l[i]==" ":
            
            # Making a shallow copy of l
            t=list(l)
            
            # Imaginarily playing x or o
            if (l.count("x")+l.count("o"))%2==0:
                t[i]="x"
            else:
                t[i]="o"
                
            # If this move ends the game: marking value directly
            if check_who_won(t)!=2:
                t[-1]=check_who_won(t)
                
            # If this move doesn't end the game: using recursion
            else:
                e=minimax(t)
                
                # Is it the chance of x or o
                if (l.count("x")+l.count("o"))%2==0:
                    t[-1]=min_ll(e)[-1] # if l was x then t must be o
                else:
                    t[-1]=max_ll(e)[-1] # if o was x then t must be x
             
             # Storing this move in d   
            d=d+[t]
    return d

# defining a function that returns max or min of list of list on the basis of the last element
def min_ll(e):
    j=0
    c=e[0][-1]
    for i in range(len(e)):
        if e[i][-1]<c:
            c=e[i][-1]
            j=i
    return e[j]

def max_ll(e):
    j=0
    c=e[0][-1]
    for i in range(len(e)):
        if e[i][-1]>c:
            c=e[i][-1]
            j=i
    return e[j]
        


if __name__=="__main__":
    main()