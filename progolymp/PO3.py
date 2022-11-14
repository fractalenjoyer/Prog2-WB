import math
f1 = lambda n: 20 + n%2*10
f2 = lambda n, m: 10*(max(0, math.ceil(m/n) - n%2))
f = lambda x, y: f1(x) + f2(x, y)

print(f(int(input("Antal med grönt kort, N ? ")), int(input("Antal utan grönt kort, M ? "))))