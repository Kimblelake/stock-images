from turtle import Turtle, Screen
from src.shapes.Square import Square

screen = Screen()

t = Turtle()
s = Square(1,1,20)
s.draw(t)
s = Square(20,20,20)
s.draw(t)
# dodgy trick to stop before closing the screen
answer = screen.numinput("a2", "oioi")
