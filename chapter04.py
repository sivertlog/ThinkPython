import turtle
import math

def jump(t:turtle.Turtle, length):
    t.penup()
    t.forward(length)
    t.pendown()

def rectangle(t,length,width):
    parallelogram(t,length,width,90)

def rhombus(t, side, angle):
    parallelogram(t, side, side, angle)

def square(t, side):
    rhombus(t, side, 90)

def parallelogram(t:turtle.Turtle, base, leg, angle):
    directives=((base, angle), (leg, 180-angle))
    for i in range(4):
        t.forward(directives[i%len(directives)][0])
        t.left(directives[i%len(directives)][1])

def draw_pie(t:turtle.Turtle, n, leg):
    base=2*leg*math.sin(math.radians(180/n))
    for side in range(n):
        triangle(t, leg, base)


def triangle(t:turtle.Turtle, leg, base,):
    a=math.degrees(math.asin(.5*base/leg))
    ta=2*a
    ba=(ta-180)/2
    t.left(a)
    t.forward(leg)
    t.left(180-ba)
    t.forward(base)
    t.left(180-ba)
    t.forward(leg)
    #ma=(180-ta)-a
    #t.left(ma+ta)
    t.left(180-a)

def polyline(t:turtle.Turtle,n,length,angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def arc(t:turtle.Turtle, radius, angle):
    arc_length = 2*math.pi*radius*angle/360
    n=30
    length=arc_length/n
    step_angle=angle/n
    polyline(t,n,length,step_angle)

def petal(t:turtle.Turtle,radius,angle):
    if angle>150:
        angle=150
    arc(t,radius,angle)
    t.left(180-angle)
    arc(t,radius,angle)

def flower(t:turtle.Turtle, radius, angle):
    start_angle=t.heading()
    count=0
    while count==0 or start_angle != t.heading():
        petal(t, radius, angle)
        count += 1

t=turtle.Turtle()
t.color("white")
t.speed(0)
t.shape("turtle")

screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
t.clear()

#flower(t, 50,30)

#triangle(t,75,30)
draw_pie(t,7,400)
rectangle(t, 40, 80)
square(t,100)
rhombus(t,70, 60)
parallelogram(t, 80, 60, 30)

turtle.exitonclick()