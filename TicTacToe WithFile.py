import random
import json
# L should be of 11 in length to store value as l[9] and list of next steps in l[10]
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
        
        

# Try to construct a minimax that returns choices of move at position l and their corresponding values
# It automatically detects whose chance it is by counting x and o in l
def main(l):
    
    # d should store the choices for the one move after l and their values as the last element of each element in d

    
    # To process every possible move and get its value
    for i in range(len(l)-2):
        
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
                t[-2]=check_who_won(t)
                
            # If this move doesn't end the game: using recursion
            else:
                t=main(t)
                # Is it the chance of x or o
                if (l.count("x")+l.count("o"))%2==0:
                    t[-2]=min_ll(t[-1]) # if l was x then e must be o
                else:
                    t[-2]=max_ll(t[-1]) # if o was x then e must be x
             # Storing this move in d   
            l[-1]=l[-1]+[t]
            #d was l[-1]
    return l

# returns list from list of list with the greatest last element (value)
def min_ll(e):
    value=e[0][-2]
    for i in range(len(e)):
        if e[i][-2]<value:
            value=e[i][-2]
    return value


# Returns list from list of list with the smallest last element (value)
def max_ll(e):
    value=e[0][-2]
    for i in range(len(e)):
        if e[i][-2]>value:
            value=e[i][-2]
    return value
            


if __name__=="__main__":
    l=[" ", "x", "o", "o", "x", " ", "x", " ", "o"," ", []]
    #l=[" ", "x", "o", "o", "x", " ", "x", " ", "o"," ", []]
    #l=[" ", " ", " ", " ", " ", " ", " ", " ", " "," ", []]
    for _ in range(9):
        with open(f'All_possible_Games_TTT{_+1}.json', 'a'):
            json.dump(main(l), f'All_possible_Games_TTT{_+1}.json')
