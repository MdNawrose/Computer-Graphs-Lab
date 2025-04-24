import turtle
t = turtle.Turtle()
t.fillcolor("green")
t.begin_fill()
for i in range(2):
  t.forward(400)
  t.left(90)
  t.forward(200)
  t.left(90)
  
t.end_fill()

t.penup()
t.forward(275)
t.left(90)
t.forward(100)
t.pendown()

t.fillcolor("red")
t.begin_fill()
t.circle(70)
t.end_fill()
turtle.mainloop()
