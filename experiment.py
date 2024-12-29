class something:
    def __init__(self):
         self.state=['x', 'x', 'o', 'o', 'x', 'x', 'x', 'o', 'o']
         self.status=self.check_who_won()
    def __str__(self):
        return self.check_who_won()
    def check_who_won(self):
            
                # Checking 3 consecutive horizontally, vertically and diagonally respectively
            for i in range(3):
                if self.state[0+3*i]==self.state[1+3*i]==self.state[2+3*i]:
                    print("abcd")
                    return 1  if self.state[0+3*i]=="x" else -1
                elif self.state[0+i]==self.state[3+i]==self.state[6+i]:
                    print("efg")

                    return 1  if self.state[0+i]=="x" else -1
            for i in range(2):
                if self.state[6*i]==self.state[4]==self.state[-6*i+8]:
                    print("hij")
                    return 1  if self.state[8*i]=="x" else -1
            # Checking if all chances are exhausted: 0 corresponds to draw
            if self.state.count("x")+self.state.count("o")==9:
                return 0
                
            # If more chances can be played: 2
            return 2
print(something().status)