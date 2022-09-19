x, y, n = map(int, input().split())
for i in range(1,n+1): print((not i%x) * "fizz" + (not i%y) * "buzz" or i)