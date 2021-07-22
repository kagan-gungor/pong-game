import turtle
import random

window = turtle.Screen()
t = turtle.Turtle()
t.dx = 0.20
t.dy = 0.20
t.speed(11)
radius = 20
color = ["green", "blue", "red", "black", "brown"]

for i in range(10):
    t.circle(radius)
    radius += 10

    t.color(random.choice(color))





while True:
    window.update()