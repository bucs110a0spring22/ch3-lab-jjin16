import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
## method 1

"""def turtle_go():
  distance_to_move_for_mic= random.randrange(1,100)
  distance_to_move_for_leo= random.randrange(1,100)
  michelangelo.fd(distance_to_move_for_mic)
  leonardo.fd(distance_to_move_for_leo)
turtle_go()
def reset_turtle():
  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)
reset_turtle() 
"""
## method 2
"""window.bgcolor("purple")
def realistic_race():
  for call in range(10):
    mic_move= random.randrange(1,10)
    leo_move= random.randrange(1,10)
    michelangelo.fd(mic_move)
    leonardo.fd(leo_move)
realistic_race()
reset_turtle()
"""
# Part B - complete part B here
window.bgcolor("white")
leonardo.pencolor("black")
def polygon(number_of_sides=1):
    inner_angle_tot= 360
    side_length= 50
    inner_angle_per= inner_angle_tot/number_of_sides
    leonardo.down()
    for i in range (number_of_sides):
      leonardo.fd(side_length)
      leonardo.rt(inner_angle_per)
    leonardo.clear()
def eqtriangle():
  polygon(3)
def square():
  polygon(4)
def hexagon():
  polygon(6)
def nonagon():
  polygon(9)
def dodecagon():
  polygon(12)
list_of_shapes= [eqtriangle(), square(), hexagon(), nonagon(), dodecagon()]
for polygon_functions in list_of_shapes:
  polygon_functions

window.exitonclick
