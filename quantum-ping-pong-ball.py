from math import pi, sqrt


h = 6.63**-34
R = 0.02
m = 0.0027
g = 9.8

hbar = h / (2 * pi)
t = sqrt(20 * g * R)
v = sqrt(20 * g * R)

distance = 2 * sqrt((hbar * t)/m)
bounces = 1

t1 = sqrt((20 * R)/g)

def print_bounces(bounce, dist):
    print('After bounce ', bounce, ' the ball has traveled ', dist, 
      ' meters.')

print_bounces(bounces, distance)

while distance < R:
    theta = distance/R
    distance = distance + v * theta * t1
    bounces += 1
    
    print_bounces(bounces, distance)
    
print('The ball fell off after ', bounces-1, ' bounces.')
