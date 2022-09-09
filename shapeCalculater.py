class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self, width, height):
        area = int(width) * int(height)
        return area

    def get_perimeter(self, width, height):
        perimeter = (width * 2) + (height * 2)
        return perimeter

    def get_diagonal(self, width, height):
        diagonal = (width ** 2) + (height ** 2) ** 0.5
        return diagonal

    def get_picture(self, width, height):
        picture = ''
        line = ''
        row = 0
        
        if int(width) > 50 or int(height) > 50 :
          return 'Too big for picture'

        while len(line) < int(width):
            line += '*'

        while row != int(height):
            picture += line + '\n'

        return picture
      
    def get_amount_inside(self):
