import random
import turtle
t = turtle.Turtle()
t.speed(0)

#firework color
def pen(color):
    t.color(color)

pen('red')

def move():
    t.pu()
    x = random.randint(-165,165)
    y = random.randint(-165,165)
    t.goto(x,y)
    t.pd()

def sky(colour):
     wn = turtle.Screen()
     wn.bgcolor(colour)

sky('black')

def firework(size):
    for num in range (20):
         t.fd(size)
         t.rt(180-(360/20))

firework(50)
move()
pen('yellow')
firework(75)
move()

pen('orange')
firework(199)   
firework(50)
move()

pen('blue')
firework(75)
move()

pen('pink')
firework(199)
firework(50)
move()

pen('yellow')
firework(75)
move()

pen('orange')
firework(199)   
firework(50)
move()

pen('blue')
firework(75)
move()

pen('pink')
firework(199)
firework(50)
move()

pen('yellow')
firework(75)
move()

pen('orange')
firework(199)   
firework(50)
move()
pen('blue')
firework(75)
move()

pen('pink')
firework(199)
firework(50)
move()

pen('yellow')
firework(75)
move()

pen('orange')
firework(199)   
firework(50)
move()

pen('blue')
firework(75)
move()

pen('pink')
firework(199)  


