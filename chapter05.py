from time import time
from turtle import Turtle, Screen

#02

def num_days(epoch_time):
    seconds_in_day=86400 #60*60*24
    return epoch_time//seconds_in_day

def current_time(epoch_time):
    hours, sec_remain=divmod(epoch_time,3600)
    minutes, seconds=divmod(sec_remain, 60)
    return f"{int(hours%24):02d}:{int(minutes):02d}:{int(seconds):02d}"


epoch_msg='Jan 1, 1970, 00:00:00 UTC'
now = time()
print(now)
print("Number of days since", epoch_msg, "is", num_days(now))
print("Current Time", current_time(now), "UTC")

#03

def is_triangle(a,b,c):
    result = True
    if a > b+c:
        result = False
    elif b > c+a:
        result = False
    elif c >a+b:
        result = False
    return "Yes" if result else "No"

def is_triangleV2(a,b,c):
    return "No" if a>b+c or b>c+a or c>a+b else "Yes"



print(is_triangle(1,2,7))
print(is_triangle(1,2,3))
print(is_triangleV2(1,2,7))
print(is_triangleV2(1,2,3))

#04

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

#05

def draw(t:Turtle, length):
    angle = 50
    factor = 0.6
    if length > 5:
        t.forward(length)
        t.left(angle)
        draw(t,factor*length)
        t.right(2*angle)
        draw(t,factor*length)
        t.left(angle)
        t.back(length)

#06
def koch(t:Turtle, x):
    angle = 60
    f = 3

    if x > 5:
        koch(t,x/f)
        t.left(angle)
        koch(t,x/f)
        t.right(2*angle)
        koch(t, x/f)
        t.left(angle)
        koch(t,x/f)
    else:
        t.forward(x)

def snowflake(t:Turtle, sides=6):
    n_koch=360//sides
    for _ in range(sides):
        koch(t, 100)
        t.right(n_koch)

#07#####From Google Gemini
def sierpinski(t:Turtle, length, depth):
  """Draws a Sierpinski triangle recursively.

  Args:
    length: The length of the sides of the triangle.
    depth: The recursion depth.
  """

  if depth == 0:
    for _ in range(3):
      t.forward(length)
      t.left(120)
  else:
    sierpinski(t,length / 2, depth - 1)
    t.forward(length / 2)
    sierpinski(t,length / 2, depth - 1)
    t.backward(length / 2)
    t.left(60)
    t.forward(length / 2)
    t.right(60)
    sierpinski(t,length / 2, depth - 1)
    t.left(60)
    t.backward(length / 2)
    t.right(60)


t=Turtle("turtle")
t.speed(0)
screen = Screen()
screen.screensize(640,400)

# 05 #
#draw(t,50)
# 06 #
#koch(t,70)
#snowflake(t,3)
# 07 #
sierpinski(t,200,3)

screen.exitonclick()