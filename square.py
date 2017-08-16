import turtle
window=turtle.Screen()
window.bgcolor("red")


def draw_square():
     brad=turtle.Turtle()
     brad.shape("turtle")
     brad.color("yellow","blue")
     brad.speed(0)
     for ct in range(0,36):
         for shape in range(0,4):
             brad.forward(100)
             brad.right(90)
         brad.right(10)


def draw_arc():

    angei=turtle.Turtle()
    angei.pu()
    angei.goto(100,100)
    angei.pd()
    angei.shape("classic")
    angei.color("green","blue")
    angei.speed(0)
    angei.circle(100)


draw_square()
draw_arc()
window.exitonclick()
