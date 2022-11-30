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
input = Inputer("uppg52.txt")

import numpy as np
from numpy.fft import fft, ifft

def main(n,m,k):
    length = 1 << (n*m).bit_length()
    f = np.pad(np.ones(m), (0, length-m), 'constant')
    out = sorted(np.trim_zeros(np.real(ifft(fft(f)**n))), reverse=True)
    return sum(out[:k])/(m**n)

while (input.lines):
    n = int(input())
    m = int(input())
    k = int(input())
    print("Svar:",main(n,m,k))