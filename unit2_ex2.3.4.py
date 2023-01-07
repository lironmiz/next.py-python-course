# exercise 2.2.4 from unit 2
'''
Look at the picture in front of you: this is a digital picture that shows: a computer, a keyboard and a mouse.

 A digital image showing: computer, keyboard and mouse
When you focus on a certain part of the image and enlarge it (see on the right side of the image) we see a sort of collection of small dots on the screen. Each point on the screen is called a pixel - a basic graphic information unit in a computer that describes a point in a digital image. Every image we see on the computer screen is made up of hundreds to tens of millions of tiny dots of pixels.

Each pixel contains the following information: its position on the screen and its color.

The location of a pixel in an image is represented by x and y coordinates.
A pixel's color is represented by three colors: red, green and blue. The color that appears on the screen is determined by three different intensities of these colors. It is customary to mark amounts of red, green and blue that must be combined together in order to create the necessary shade. Determining the intensities of the various color components is done by assigning the integers between 0 and 255 to each of the colors - where 0 means not to illuminate the pixel at all, and 255 signifies illumination at full intensity.
Create a class called Pixel to represent a pixel, which includes the features described earlier:

"""
_x - x coordinate
_y - y coordinate
_red - a value between 0 and 255
_green - a value between 0 and 255
_blue - a value between 0 and 255
"""
Add an initialization method to the class that initializes the position and color attributes - initialize the attributes to the default value 0.

Add to the class an instance method named set_coords defined as follows:

def set_coords(self, x, y):
The function receives a parameter containing values for x_ and y_ attributes and determines their value.

Add an instance method called set_grayscale to the class defined as follows:

def set_grayscale(self):
The method takes a pixel and changes its color to gray. Do it as follows:

Calculate the average value of the red, green and blue color features of the pixel.
Placement of the average result obtained in section (a) in each of the color properties.

Add to the class an instance method named print_pixel_info defined as follows:

def print_pixel_info(self):
The method prints information about the fiscal in the following format:

my_pixel.print_pixel_info()
X: 5, Y: 6, Color: (0, 55, 78)
The order of colors in printing is: red, green, blue.

If two colors in a pixel have a value equal to 0, and the value of the third pixel color is greater than 50, add the name of the color whose value is not zero at the end of the printout. for example:

my_pixel.print_pixel_info()
X: 5, Y: 6, Color: (0,55,0) Green

Write a main program that includes creating an instance of a pixel with the following values:
x value of 5.
y value of 6.
Value of red color 250.
Value of green color 0.
Value of blue color 0.
Print information about the pixel by calling the print_pixel_info instance method.
Call the set_grayscale instance method.
Print information about the pixel by calling the print_pixel_info method again.
If you implemented the code correctly, the output of the program should look like this.

To view an accessible code snippet
p = Pixel(5, 6, 250)
p.print_pixel_info()
p.set_grayscale()
p.print_pixel_info()
'''


class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average = (self._red + self._green + self._blue) // 3
        self._red = average
        self._green = average
        self._blue = average

    def print_pixel_info(self):
        color = (self._red, self._green, self._blue)
        color_name = None
        if self._red == 0 and self._green == 0 and self._blue > 50:
            color_name = "Blue"
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            color_name = "Green"
        elif self._red > 50 and self._green == 0 and self._blue == 0:
            color_name = "Red"
        print(f"X: {self._x}, Y: {self._y}, Color: {color} {color_name}")


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == '__main__':
    main()
