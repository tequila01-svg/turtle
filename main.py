import turtle

#creating a canvas
turtle.Screen().bgcolor("blue")
sc=turtle.Screen()
sc.setup(400,300)
turtle.title("welcome to turtle windows!!")
board=turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i=1+1
turtle.done