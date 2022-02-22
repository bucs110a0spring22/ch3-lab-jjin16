import turtle               #1. import modules
import random
import time

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')
COLORMODE=255
window.colormode(COLORMODE)


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
    if hidden_or_shown == True:
        michelangelo.st()
        leonardo.st()
    else:
        michelangelo.ht()
        leonardo.ht()
def reset_turtle():
  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)
def winner_announce():
    turtle_visibility(False)
    if michelangelo.distance(-100, 20) > leonardo.distance(-100, -20):
        michelangelo.write("Michelangelo wins! orange wins!",False ,"left" ,('Arial', 20, 'normal'))
    elif michelangelo.distance(-100, 20) < leonardo.distance(-100, -20):
        leonardo.write("Leonardo wins! blue wins!",False ,"left" ,('Arial', 20, 'normal'))
    elif michelangelo.distance(-100, 20) == leonardo.distance(-100, -20):
        michelangelo.write("draw! no one wins!",False ,"left" ,('Arial', 20, 'normal'))
        leonardo.write("draw! no one wins!",False ,"left" ,('Arial', 20, 'normal'))
    pause_second= 3
    time.sleep(pause_second)
    turtle_visibility(True)
    leonardo.clear()
    michelangelo.clear()
turtle_go()    
winner_announce()    
reset_turtle()
## method 2
RGB_FOR_LIGHT_PURPLE= [236, 192, 250]
window.bgcolor(RGB_FOR_LIGHT_PURPLE)
#window.bgcolor((236, 192, 250))
def realistic_race():
  number_of_calls= 10
  for call in range(number_of_calls):
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
def polygon(number_of_sides=3):
    inner_angle_tot= 360
    side_length= 50
    inner_angle_per= inner_angle_tot/number_of_sides
    leonardo.down()
    for lines in range (number_of_sides):
      leonardo.fd(side_length)
      leonardo.rt(inner_angle_per)
    leonardo.clear()
def eqtriangle():
  three_sides=3
  polygon(three_sides)
def square():
  four_sides=4
  polygon(four_sides)
def hexagon():
  six_sides=6
  polygon(six_sides)
def nonagon():
  nine_sides=9
  polygon(nine_sides)
def dodecagon():
  twelve=12
  polygon(twelve)

list_of_shapes= [eqtriangle(), square(), hexagon(), nonagon(), dodecagon()]
for polygon_functions in list_of_shapes:
  polygon_functions

window.exitonclick()