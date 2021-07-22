import turtle
pen=turtle.Turtle()
#creates turtle called pen
turtle.tracer(0,0)
#allows turtle to draw faster
pen.width(2)
def king(x,y,color):
  #function draws king in any location on the board. 
  pen.setheading(0)
  pen.penup()
  pen.color("blue")
  pen.fillcolor(color)
  pen.begin_fill()
  pen.goto(x*40-177.5,y*40-167.5)
  pen.pendown()
  pen.right(90)
  pen.forward(5)
  pen.left(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(5)
  pen.left(90)
  pen.forward(15)
  pen.left(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(15)
  pen.right(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(5)
  pen.left(90)
  pen.forward(15)
  pen.left(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(5)
  pen.left(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(5)
  pen.end_fill()
  pen.penup()
  pen.goto(1000,1000)
  turtle.update()
def pawn(x,y,color):
  #adds pawn
  pen.setheading(0)
  pen.penup()
  pen.color("blue")
  pen.fillcolor(color)
  pen.begin_fill()
  pen.goto(-185+40*x,-170+40*y)
  pen.pendown()
  pen.forward(10)
  pen.right(90)
  pen.forward(10)
  pen.right(90)
  pen.forward(2.5)
  pen.left(90)
  pen.forward(15)
  pen.left(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(15)
  pen.right(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(5)
  pen.left(90)
  pen.forward(15)
  pen.left(90)
  pen.forward(2.5)
  pen.right(90)
  pen.forward(10)
  pen.right(90)
  pen.end_fill()
  pen.penup()
  pen.goto(500,500)
  turtle.update()
def drawboard():
  pen.color("white")
  pen.dot(5000)
  pen.color("black")
  for f in range (9):
    pen.penup()
    pen.goto(-160+40*f,-160)
    pen.pendown()
    pen.goto(-160+40*f,160)
  for i in range (8):
    for t in range (4):
      pen.penup()
      if i%2==1:
        pen.goto(-80+80*t,-160+40*i)
      if i%2==0:
        pen.goto(-120+80*t,-160+40*i)
      pen.pendown()
      pen.fillcolor("black")
      pen.begin_fill()
      for z in range (4):
        pen.forward(40)
        pen.left(90)
      pen.end_fill()
  for i in range (9):
    pen.penup()
    pen.goto(-160,-160+40*i)
    pen.pendown()
    pen.goto(160,-160+40*i)
  turtle.update()
def queen(x,y,color):
  pen.setheading(0)
  pen.penup()
  pen.goto(-180+40*x,-161+40*y)
  pen.color("blue")
  pen.fillcolor(color)
  pen.begin_fill()
  pen.pendown()
  for i in range(45):
    pen.fd(0.2)
    pen.right(2)
  pen.right(90)
  pen.fd(2.5)
  pen.left(90)
  pen.fd(5)
  pen.left(90)
  pen.fd(2.5)
  pen.right(90)
  pen.fd(20)
  pen.left(90)
  pen.fd(5)
  pen.right(90)
  pen.fd(5)
  pen.right(90)
  pen.fd(20)
  pen.right(90)
  pen.fd(5)
  pen.right(90)
  pen.fd(5)
  pen.left(90)
  pen.fd(20)
  pen.right(90)
  pen.fd(5)
  pen.left(90)
  pen.fd(5)
  pen.left(90)
  pen.fd(5)
  pen.right(90)
  for i in range(45):
    pen.fd(0.2)
    pen.right(2)
  pen.end_fill()
  turtle.update()
def rook(x,y,color):
  pen.setheading(0)
  pen.penup()
  pen.goto(-192.5+40*x,-170+40*y)
  pen.begin_fill()
  pen.color("blue")
  pen.fillcolor(color)
  pen.pendown()
  pen.forward(10)
  pen.right(90)
  pen.forward(5)
  pen.left(90)
  pen.forward(5)
  pen.left(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(10)
  pen.right(90)
  pen.forward(25)
  pen.right(90)
  pen.forward(25)
  pen.right(90)
  pen.forward(25)
  pen.right(90)
  pen.end_fill()
  turtle.update()
def bishop(x,y,color):
  pen.setheading(0)
  pen.penup()
  pen.goto(-182.5+40*x,-170+40*y)
  pen.begin_fill()
  pen.color("blue")
  pen.fillcolor(color)
  pen.pendown()
  pen.forward(5)
  pen.right(90)
  for i in range(5):
    pen.forward(5)
    pen.left(90)
    pen.forward(2.5)
    pen.right(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(35)
  pen.right(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(5)
  pen.left(90)
  for i in range(5):
    pen.forward(5)
    pen.right(90)
    pen.forward(2.5)
    pen.left(90)
  pen.end_fill()
  pen.penup()
  pen.goto(1000,1000)
  turtle.update()
def knight(x,y,color):
  pen.setheading(0)
  pen.penup()
  pen.goto(-192.5+40*x,-170+40*y)
  pen.begin_fill()
  pen.color("blue")
  pen.fillcolor(color)
  pen.pendown()
  pen.forward(15)
  pen.right(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(10)
  pen.left(90)
  pen.forward(20)
  pen.right(90)
  pen.forward(5)
  pen.right(90)
  pen.forward(25)
  pen.right(90)
  pen.penup()
  pen.end_fill()
  turtle.update()