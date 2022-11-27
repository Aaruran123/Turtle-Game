import time
import turtle
from turtle import Turtle
from random import randint

#window setup
loadWindow = turtle.Screen()
turtle.bgcolor("#FFE879")
turtle.color("#FFE873")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.color("dark blue")
turtle.write("Racing Turtles","black",align=('Left'),font=('bold',30))

#Finish Line
Size_of_the_Stamp =20
Size_of_the_square=15
Finish_Line=200
turtle.color("black")
turtle.shape("square")
turtle.goto(-300,300)
turtle.shapesize(Size_of_the_square/Size_of_the_Stamp)
turtle.penup
for i in range (11):
    turtle.setpos(Finish_Line,(150-(i*Size_of_the_square*2)))
    turtle.stamp()
turtle.hideturtle()

# Racing lines
td1=turtle.Pen()
td1.hideturtle()
td1.up()
td1.goto(-250,0)
td1.down()
td1.pencolor("black")
td1.pensize(6)
td1.forward(450)
td2=turtle.Pen()
td2.hideturtle()
td2.up()
td2.goto(-200,150)
td2.down()
td2.pencolor("black")
td2.pensize(6)
td2.right(90)
td2.forward(300)

#Turtle Design
turtle1=turtle.Pen()
turtle1.shape("turtle")
turtle1.color("#A52A2A")

turtle2=turtle.Pen()
turtle2.shape("turtle")
turtle2.color("#00FF00")
turtle1.up()
turtle1.goto(-250,-100)
turtle1.down()
turtle2.up()
turtle2.goto(-250,100)
turtle2.down()
turtle.hideturtle()
time.sleep(1)

#Turtle Race
for i in range (145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
turtle.hideturtle()
turtle.exitonclick() #once a turtle (out of two) wins the program will stop 