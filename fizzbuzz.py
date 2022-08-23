x, y, n = input().split()
for i in range(n): print((not i%x) * "fizz" + (not i%y) * "buzz" or i)