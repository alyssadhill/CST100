class Rectangle:
    """ Rectangle class for representing and manipulating x,y,width,height coordinates."""
    def __init__(self, initX, initY, initWidth, initHeight):
        self.x = initX
        self.y = initY
        self.width = initWidth
        self.height = initHeight

    # concatenate attributes into a string
    def __str__(self):
        attributes = str(self.x) + ", " + str(self.y) + ", " + str(self.width) + ", " + str(self.height)
        return "Rectangle("+ attributes + ")"
    
    # find x coordinate of the right side of rectangle
    def right (self):
        return self.x + self.width
    
    # find y coordinate of the bottom side of rectangle
    def bottom(self):
        return self.y + self.height
    
    # return height and width of a rectangle 
    def size(self):
        return self.width, self.height

    # return x and y coordinates
    def position(self):
        return self.x, self.y

    # find the area of a rectangle 
    def area(self):
        return self.width * self.height

    # take an offset value and returns a copy of the rectangle expanded in all directions
    def expand(self, offset):
        offsetX = self.x - offset
        offsetY = self.y - offset
        offsetWidth = self.width + (offset * 2)
        offsetHeight = self.height + (offset * 2)
        return Rectangle(offsetX, offsetY, offsetWidth, offsetHeight)
    
    # take coordinates x and y and returns True if point is inside or on edge of rectangle, False if it is not
    def contains_point(self, x, y):
        if x >= self.x and y >= self.y and x <= self.width + self.x and y <= self.height + self.y:
            return True
        else:
            return False
