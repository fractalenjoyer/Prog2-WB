n, q = map(int, input().split())

class People:
    def __init__(self, default = 0):
        self.people = dict()
        self.default = default
    
    def __getitem__(self, i):
        if i in self.people:
            return self.people[i]
        else:
            return self.default
    
    def __setitem__(self, i, v):
        self.people[i] = v
        
people = People(0)

for _ in range(q):
    command, *args = input().split()
    if command == "SET":
        people[args[0]] = int(args[1])
    elif command == "PRINT":
        print(people[args[0]])
    elif command == "RESTART":
        people = People(args[0])