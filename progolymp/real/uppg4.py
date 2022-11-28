"""
This one may work with some further tweaking
"""

class Inputer:
    def __init__(self, file):
        with open(file, "r") as f:
            self.lines = [line.strip() for line in f][::-1]
        self.remaining = len(self.lines)

    def __call__(self, *args):
        if self.remaining  == 0:
            return None
        self.remaining -= 1
        return self.lines.pop()

# put in test file name
input = Inputer("uppg4.txt")

from sympy.solvers.diophantine import diophantine
from sympy import symbols

def main():
    counts = [int(input()) for i in range(4)]
    count = sum(counts)
    strength = int(sum([(k+1)*v for k,v in enumerate(counts)])/2)   
    x, y, z = symbols("x, y, z", integer=True)
    print(diophantine(count+x+2*y+3*z-strength))
    
    
        


while input.lines:
    main()