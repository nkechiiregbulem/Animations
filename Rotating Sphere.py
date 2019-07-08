#Please install Processing, then run code to get a rotating sphere


from math import pi
from random import randint

def setup():
    global sphere_size
    size(400, 400, P3D)
    sphere_size = randint(100, 200)
    
def draw():
    global sphere_size
    background(1)
    translate(width / 2, height / 2, 0)
    rotateX(float(mouseX) / width * 2 * pi)
    rotateY(float(frameCount) / 200)
    noFill()
    stroke(255)
    sphere(sphere_size)
