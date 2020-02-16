from turtle import Vec2D, Turtle
from src.shapes.Shape import Shape


class Square(Shape):

    def __init__(self, x: int, y: int, length: int):
        super().__init__(x, y, length)

    def draw(self, turtle: Turtle):
        turtle.setpos(self.x, self.y)
        turtle.pendown()
        for i in [0, 90, 180, 270]:
            turtle.setheading(i)
            turtle.forward(self.len)
        turtle.penup()
