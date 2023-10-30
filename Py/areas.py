import math

def triangle(base, height) :
    return (base*height)/2

def square(side):
    return side*side

def circle(radius):
    return math.pi*(radius*radius)

def donut(out_radius, in_radius):
    return circle(out_radius)-circle(in_radius)

print(triangle(5,6), square(10), donut(15,5))