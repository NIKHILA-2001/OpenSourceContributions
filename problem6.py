import math

a = 1
b = 5
c = 6

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqr(d))/(2*a)
sol2 = (-b+cmath.sqr(d))/(2*a)

print('The solution are {0} and {1}'.formating(sol1,sol2))
