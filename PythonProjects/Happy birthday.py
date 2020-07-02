# implementing turtle graphics following a tutorial
# Program prints Happy Birthday

import turtle

happy = turtle.Screen()
happy.bgcolor("black")
turtle = turtle.Turtle()
turtle.shape("circle")
turtle.color("peru")
turtle.width(9)
turtle.speed(11)
colors = ["peru", "ivory", "dark orange", "coral", "cyan", "hot pink", "gold", "ivory", "yellow", "red", "pink",
          "green", "blue", "light blue", "light green", ]


def move(x, y):
    turtle.up()
    turtle.setposition(0, 0)
    turtle.setheading(90)
    turtle.rt(90)
    turtle.fd(x)
    turtle.lt(90)
    turtle.fd(y)
    turtle.pendown()


def mov(x, y):
    turtle.up()
    turtle.setposition(0, 0)
    turtle.setheading(90)
    turtle.lt(90)
    turtle.fd(x)
    turtle.rt(90)
    turtle.fd(y)
    turtle.pendown()


def K():
    turtle.fd(80)
    turtle.backward(50)
    turtle.rt(45)
    turtle.fd(70)
    turtle.backward(50)
    turtle.rt(97)
    turtle.fd(60)


def talloval(r):
    turtle.left(45)
    for loop in range(2):
        turtle.circle(r, 90)


def O(r):
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r, 90)
        turtle.circle(r / 2, 90)


def U():
    turtle.lt(90)
    for i in range(5):
        turtle.rt(5)
        turtle.fd(5)
    turtle.rt(65)
    turtle.fd(68)
    mov(160, 400)
    turtle.rt(90)
    for i in range(5):
        turtle.lt(5)
        turtle.fd(5)
    turtle.lt(65)
    turtle.fd(68)


def N():
    turtle.fd(76)
    turtle.lt(35)
    turtle.backward(94)
    turtle.rt(35)
    turtle.fd(76)


def ballon(size):
    turtle.color(colors[size % 9])
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.rt(90)
    turtle.fd(90)


def draw_happy(i, x, y):
    turtle.pencolor("linen")
    turtle.color(colors[i % 7])
    turtle.begin_fill()
    turtle.lt(70)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(33)
    turtle.end_fill()


def f1():
    for i in range(9):
        turtle.pensize(5)
        turtle.pencolor('light blue')
        turtle.color(colors[i % 19])
        turtle.begin_fill()
        turtle.left(330)
        turtle.forward(55)
        turtle.begin_fill()
        turtle.rt(110)
        turtle.circle(33)
        turtle.end_fill()
        turtle.rt(11)
        turtle.backward(33)
        turtle.end_fill()


def cake(x, y):
    turtle.fd(x)
    turtle.rt(90)
    turtle.fd(y)
    turtle.rt(90)
    turtle.fd(x)
    turtle.rt(90)
    turtle.fd(y)


def heart():
    for i in range(43):
        turtle.pencolor(colors[i % 9])
        turtle.rt(5)
        turtle.fd(5)

    turtle.fd(150)
    turtle.penup()
    turtle.rt(140)
    turtle.fd(147)
    turtle.pendown()
    for i in range(43):
        turtle.pencolor(colors[i % 9])
        turtle.lt(5)
        turtle.fd(5)
    turtle.lt(7)
    turtle.fd(151)


def A(size):
    turtle.rt(16)
    turtle.forward(size)
    turtle.rt(150)
    turtle.fd(size)
    turtle.backward(size / 2)
    turtle.rt(105)
    turtle.fd(size / 3)


def B():
    turtle.forward(60)
    turtle.rt(90)
    for i in range(18):
        turtle.rt(9)
        turtle.fd(3)
    for i in range(18):
        turtle.rt(13)
        turtle.backward(3)


def C():
    turtle.circle(2)

    for i in range(40):
        turtle.lt(5)
        turtle.backward(5)


def d(size):
    turtle.fd(size)
    turtle.backward(size)
    turtle.lt(90)
    turtle.fd(26)
    for i in range(15):
        turtle.rt(12)
        turtle.fd(4)
    turtle.fd(14)


def i(size):
    turtle.fd(size)


def t(size):
    turtle.fd(size)
    turtle.backward(size / 2)
    turtle.lt(90)
    turtle.fd(10)
    turtle.backward(20)


def H():
    turtle.fd(60)
    turtle.backward(30)
    turtle.rt(90)
    turtle.fd(30)
    turtle.lt(90)
    turtle.fd(30)
    turtle.backward(60)


def P():
    turtle.fd(60)
    turtle.rt(90)
    turtle.fd(7)
    for i in range(8):
        turtle.rt(20)
        turtle.fd(5)


def Y():
    turtle.fd(40)
    turtle.left(60)
    turtle.fd(20)
    turtle.backward(20)
    turtle.rt(90)
    turtle.fd(35)


def Y2():
    turtle.fd(50)
    turtle.left(60)
    turtle.fd(30)
    turtle.backward(30)
    turtle.rt(90)
    turtle.fd(55)


def R():
    turtle.fd(60)
    turtle.rt(90)
    turtle.fd(7)
    for i in range(15):
        turtle.rt(12)
        turtle.fd(3)
    turtle.lt(120)
    turtle.fd(49)


def D():
    turtle.fd(60)
    turtle.rt(90)
    turtle.fd(9)
    for i in range(13):
        turtle.rt(13)
        turtle.fd(7)


def D2():
    turtle.fd(76)
    turtle.rt(90)
    turtle.fd(15)
    for i in range(13):
        turtle.rt(15)
        turtle.fd(11)


def L():
    turtle.forward(50)
    turtle.back(50)
    turtle.right(90)
    turtle.forward(40)
    turtle.penup()
    turtle.forward(10)
    '''
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(40)
    turtle.back(20)
    for i in range(8):
        turtle.rt(20)
        turtle.fd(5)
'''


def V():
    turtle.left(25)
    turtle.fd(50)
    turtle.backward(50)
    turtle.rt(50)
    turtle.fd(50)


turtle.pencolor("cyan")
turtle.width(11)
mov(220, 300)
H()
mov(180, 300)
A(65)
mov(135, 300)
P()
mov(100, 300)
P()
mov(52, 300)
Y()
mov(28, 300)
B()
move(12, 300)
i(60)
move(36, 300)
R()
move(80, 300)
t(100)
move(102, 300)
H()
move(150, 300)
D()
move(190, 300)
A(65)
move(250, 300)
Y()
turtle.pencolor("hot pink")
turtle.width(15)
mov(275, 400)
P()
mov(228, 400)
A(49)
mov(166, 400)
L()
mov(100, 400)
L()
mov(40, 400)
A(49)
move(30, 405)
V()
move(75, 400)
i(60)

turtle.speed(12)
mov(120, 20)
turtle.width(17)
turtle.color(colors[8 % 5])
turtle.begin_fill()
cake(40, 180)
turtle.end_fill()
mov(110, 55)
turtle.color(colors[8 % 3])
turtle.begin_fill()
cake(40, 160)
turtle.end_fill()
mov(100, 90)
turtle.color("hot pink")
turtle.begin_fill()
cake(40, 140)
turtle.end_fill()
mov(30, 133)
turtle.width(11)
turtle.pencolor("red")
turtle.circle(7)
move(240, 547)
f1()
mov(280, 547)
f1()
mov(0, 0)
for i in range(5):
    draw_happy(i, -189, 200)

for i in range(6):
    draw_happy(i, 189, 200)
for i in range(7):
    draw_happy(i, 123, -100)
for i in range(5):
    draw_happy(i, -123, -100)
mov(13, -80)
turtle.width(19)
heart()
mov(0, -400)
f1()

happy.exitonclick()
