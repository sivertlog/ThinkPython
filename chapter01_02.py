import math

###########
#chapter01#
###########

###1.9.2###
print(round(42.5))
print(round(43.5))
###1.9.3###
a=2++3
print(a)
#4 2 syntax error
#round(2,3 syntax error
###1.9.4###
print(type(765))
print(type(2.718))
print(type("2 pi"))
print(type(abs(-7)))
print(type(abs(-7.0)))
print(type(abs))
print(type(int))
print(type(type))
###1.9.5###
#1
min=sec=42
time=min*60+sec
print(time, "seconds in", min, "minutes and ", sec, "seconds")
#2
k=10
mile=k/1.61
print(mile)
#3
pace=time/mile
print(pace, "seconds per mile")
#4
print(min/mile, "minutes and", sec/mile, "seconds per mile")
#5
hours=time/3600
speed=mile/hours
print(speed, "miles per hour")

###########
#chapter02#
###########

#17=n not legal
x=y=1 #legal
nothing=1;
#print(nothing). #syntax error
#import maath no module named 'maath'

#1
r=5
v=4/3*math.pi*r**2
print("The volume of a sphere with a radius of", r, "centimeters is", v, "cubic centimeters.")
#2
x=42
a=math.sqrt(math.cos(x)**2+math.sin(x)**2)
print(a)
#3
print(math.e**2)
print(math.pow(math.e, 2))
print(math.exp(2))
