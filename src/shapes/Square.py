from turtle import Vec2D, Turtle


class Square:

    def __init__(self, x: int, y: int, length: int):
        self.x = x  # x co-ordinate of the leftmost part of the shape
        self.y = y  # y co-ordinate of the topmost part of the shape
        self.len = length  # length of side of square
        self.vec2D = Vec2D(x, y)

    def draw(self, turtle: Turtle):
        turtle.setpos(self.x, self.y)
        turtle.pendown()
        for i in [0, 90, 180, 270]:
            turtle.setheading(i)
            turtle.forward(self.len)
        turtle.penup()
