import sys
from turtle import Screen

screen = Screen()


print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))

from turtle import Turtle
from src.shapes.Square import Square

t = Turtle()
s = Square(1,1,20)
s.draw(t)
s = Square(20,20,20)
s.draw(t)
# dodgy trick to stop before closing the screen
answer = screen.numinput("a2", "oioi")
