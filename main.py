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

def turtle_go():
  distance_to_move_for_mic= random.randrange(1,100)
  distance_to_move_for_leo= random.randrange(1,100)
  michelangelo.fd(distance_to_move_for_mic)
  leonardo.fd(distance_to_move_for_leo)
turtle_go()
def reset_turtle():
  michelangelo.goto(-100,20)
  leonardo.goto(-100,-20)
reset_turtle() 

## method 2
window.bgcolor("purple")
def realistic_race():
  for call in range(10):
    mic_move= random.randrange(1,10)
    leo_move= random.randrange(1,10)
    michelangelo.fd(mic_move)
    leonardo.fd(leo_move)
realistic_race()
# Part B - complete part B here


window.exitonclick()
