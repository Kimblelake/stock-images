from turtle import Vec2D, Turtle


class Shape:

    def __init__(self, x: int, y: int, length: int):
        self.x = x  # x co-ordinate of the leftmost part of the shape
        self.y = y  # y co-ordinate of the topmost part of the shape
        self.len = length  # length of side of square
        self.vec2D = Vec2D(x, y)