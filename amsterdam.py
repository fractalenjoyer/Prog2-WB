from math import pi
m, n, r = map(float, input().split())
ax, ay, bx, by = map(int, input().split())

def pointdist(ax, ay, bx, by):
    return abs(ay - by) * r / n + r*min(ay, by)*abs(ax-bx)*pi/(n*m)

print(min((ay + by)*r/n , pointdist(ax, ay, bx, by)))