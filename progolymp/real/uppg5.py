"""
Slow as hell, but kinda works?
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
input = Inputer("uppg5.txt")

import sympy as sp

def main():
    x = sp.Symbol('x')
    n = int(input())
    m = int(input())
    k = int(input())
    eq = sp.parse_expr("+".join([f"x**{i}" for i in range(m)]))
    coeff = sorted(sp.Poly(eq**n, x).coeffs())
    print("Svar:",float(sum(coeff.pop()/(m**n) for _ in range(k))))

while (input.lines):
    main()    
