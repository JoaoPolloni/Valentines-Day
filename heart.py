import turtle
 window = turtle.Screen()
 window.bgcolor("pink")
 window.title("Feliz Dia dos Namorados")

 pen = turtle.Turtle()
 pen.color("red")
 pen.fillcolor("red")
 pen.pensize(3)
 pen.speed(7)

 pen.begin_fill()
 pen.left(140)
 pen.forward(224)
 for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.forward(224)
pen.end_fill()


pen.up()
pen.goto(0, -70)
pen.down()
pen.color("black")
pen.write("Para você que roubou meu coração, Feliz Dia dos Namorados, Meu Amor"
            align="center", font=("Arial", 16, "bold"))

pen.hideturtle()
turtle.done()