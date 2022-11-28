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
input = Inputer("uppg1.txt")

def main():
    count_t = 0
    count_m = 0
    left = 40
    t = int(input())
    m = int(input())
    n = 0
    while left > 0:
        eat = 0
        if n % t == 0:
            count_t += 1
            eat += 1
        if n % m == 0:
            count_m += 1
            eat += 1
        if eat > left:
            count_m -= 1
            count_t -= 1
            break
        left -= eat
        n += 1
    print(f"Svar: Tor {count_t}, Mor {count_m}")

while (input.lines):
    main()