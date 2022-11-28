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

input = Inputer("test.ini")

print()