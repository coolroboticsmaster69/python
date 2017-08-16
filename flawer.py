import turtle
import vidit

window=turtle.Screen()
window.bgcolor("red")

def jao(x,y,fla):
    fla.pu()
    fla.goto(x,y)
    fla.pd()


def draw_flawer(x,y):
    fla=turtle.Turtle()
    fla.shape("turtle")
    fla.color("yellow","blue")
    fla.speed(0)
    jao(x,y,fla)
    for ct in range(0,36):
        fla.circle(50)
        fla.right(10)
    fla.right(90)
    fla.forward(300)

def draw_square(x,y):
     brad=turtle.Turtle()
     brad.shape("square")
     brad.color("yellow","blue")
     brad.speed(0)
     jao(x,y,brad)
     for ct in range(0,36):
         for shape in range(0,4):
             brad.forward(100)
             brad.right(90)
         brad.right(10)
         brad.forward(100)
def startDrawing():
    draw_flawer(0,0)
    draw_flawer(200,200)
    draw_flawer(200,-200)
    draw_flawer(-200,200)
    draw_flawer(-200,-200)
    draw_square(300,0)
    draw_square(0,300)
    draw_square(-300,0)
    draw_square(0,-300)
    draw_square(0,0)

if __name__ == "__main__":

    startDrawing()
    window.exitonclick()
