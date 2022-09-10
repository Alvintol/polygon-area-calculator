class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = int(self.width) * int(self.height)
        return area

    def get_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2) + (self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        picture = ''
        line = ''
        row = 0

        if int(self.width) > 50 or int(self.height) > 50:
            return 'Too big for picture'

        while len(line) < int(self.width):
            line += '*'

        while row != int(self.height):
            picture += line + '\n'

        return picture

    def get_amount_inside(self, shape):
        widthToFit = 0;
        heightToFit = 0;
        
        widthToFit = int(int(self.width) / int(shape.width)) 
        heightToFit = int(int(self.height) / int(shape.height)) 
        
        return widthToFit * heightToFit
