import turtle

screen=turtle.Screen()
screen.bgcolor("white")


eye_turtle=turtle.Turtle()
eye_turtle.speed(2)

def draw_eye(x,y,radius):
    eye_turtle.penup()
    eye_turtle.goto(x,y-radius)
    eye_turtle.pendown()
    eye_turtle.fillcolor("black")
    eye_turtle.begin_fill()
    eye_turtle.circle(radius)
    eye_turtle.end_fill()
draw_eye(-50,0,30)
draw_eye(50,0,30)

screen.exitonclick()