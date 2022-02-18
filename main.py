import turtle               #1. import modules
import random
import time

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')
window.colormode(255)

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

def turtle_go():
  distance_to_move_for_mic= random.randrange(1,100)
  distance_to_move_for_leo= random.randrange(1,100)
  michelangelo.fd(distance_to_move_for_mic)
  leonardo.fd(distance_to_move_for_leo)
def turtle_visibility(hidden_or_shown):
    if hidden_or_shown == 1:
        michelangelo.st()
        leonardo.st()
    else:
        michelangelo.ht()
        leonardo.ht()
turtle_go()

def reset_turtle():
  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)
def winner_announce():
    turtle_visibility(0)
    if michelangelo.distance(-100, 20) > leonardo.distance(-100, -20):
        michelangelo.write("Michelangelo wins! orange wins!",False ,"left" ,('Arial', 20, 'normal'))
    elif michelangelo.distance(-100, 20) < leonardo.distance(-100, -20):
        leonardo.write("Leonardo wins! blue wins!",False ,"left" ,('Arial', 20, 'normal'))
    elif michelangelo.distance(-100, 20) == leonardo.distance(-100, -20):
        michelangelo.write("draw! no one wins!",False ,"left" ,('Arial', 20, 'normal'))
        leonardo.write("draw! no one wins!",False ,"left" ,('Arial', 20, 'normal'))
    time.sleep(3)
    turtle_visibility(1)
    leonardo.clear()
    michelangelo.clear()

    
winner_announce()    
reset_turtle()
## method 2
window.bgcolor((236, 192, 250))
def realistic_race():
  for call in range(10):
    mic_move= random.randrange(1,10)
    leo_move= random.randrange(1,10)
    michelangelo.fd(mic_move)
    leonardo.fd(leo_move)
realistic_race()
winner_announce()
reset_turtle()

# Part B - complete part B here
window.bgcolor("white")
leonardo.pencolor("black")
def polygon(number_of_sides=1):
    inner_angle_tot= 360
    side_length= 50
    inner_angle_per= inner_angle_tot/number_of_sides
    leonardo.down()
    for lines in range (number_of_sides):
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

window.exitonclick()