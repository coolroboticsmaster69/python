import turtle
window=turtle.Screen()
window.bgcolor("red")

def jao(x,y,ved):
    ved.pu()
    ved.goto(x,y)
    ved.pd()

def drawV(ved):
    ved.left(120)
    ved.forward(120)
    jao(-200,0,ved)
    ved.right(60)
    ved.forward(120)
def drawI(ved):
    ved.left(30)
    ved.forward(100)

def draw_d(ved):
    ved.forward(100)
    jao(-30,0,ved)
    ved.right(-270)
    ved.circle(50,180)
def draw_t(ved):
    ved.right(30)
    drawI(ved)
    ved.left(90)
    ved.backward(50)
    ved.forward(100)


def drawVidit():
    ved=turtle.Turtle()
    ved.shape("turtle")
    ved.color("yellow","blue")
    ved.speed(6)
    jao(-200,0,ved)
    drawV(ved)
    jao(-100,0,ved)
    drawI(ved)
    jao(-30,0,ved)
    draw_d(ved)
    jao(60,0,ved)
    ved.right(120)
    drawI(ved)
    jao(140,0,ved)
    draw_t(ved)

if __name__ == "__main__":
    drawVidit()
    window.exitonclick()
