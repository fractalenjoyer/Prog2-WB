"""
No idea honestly
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
input = Inputer("uppg2.txt")

import re
from itertools import combinations

def main():
    string = input()
    count = len(re.findall(r"[12]0", string))
    string = re.sub(r"[12]0", "", string)
    #regex = re.compile(r"[12]+[1-9]")

    for k,v in enumerate(string[:-1]):
        if v in "12" and string[k+1] in "123456789":
            count += 2
        else:
            count += 1
    

    
    print(f"Svar: {count}", string)


        


while (input.lines):
    main()