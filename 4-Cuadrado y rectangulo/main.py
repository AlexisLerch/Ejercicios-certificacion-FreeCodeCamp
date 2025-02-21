class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height   

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    
    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        else:
            picture = ''
        for i in range(0,self.height):
            picture += "*"*self.width+'\n'
        return picture
    
    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())

    def get_amount_inside(self, shape):
        times = 0 
        if (shape.width < self.width) and (shape.height < self.height):
            times = (self.height // shape.height)*(self.width // shape.width)
            return times
        else:
            times = 0 
            return times
    

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
