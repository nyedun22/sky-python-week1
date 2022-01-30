# Exercise 9 - Variables

# Tasks
# Part 3: Practice with complex maths

import math

g = 9.81 # m/s
v0 = 44 # m/s
theta = 80 * (math.pi / 180) # radians
x = 0.5 # m
y0 = 1 # m

height_projectile = y0 + (x*math.tan(theta)) - ( (g*(x**2) ) / ( 2 * ((v0*math.cos(theta))**2) ) )

print(height_projectile)