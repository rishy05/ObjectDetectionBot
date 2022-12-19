import turtle
from PIL import Image as img




# Create a turtle object
t = turtle.Turtle()
turtle.colormode(255)# Set the turtle's speed
t.speed(0)

# Load the image
image = img.open('pic.jpg')

# Get the size of the image
width, height = image.size

# Set the turtle's screen size to match the image size
turtle.setup(width, height)

# Set the turtle's pen size
t.pensize(1)

# Iterate through each pixel in the image
for x in range(width):
    for y in range(height):
        # Get the pixel color at (x, y)
        r, g, b = image.getpixel((x, y))

        # Set the turtle's pen color to the pixel color
        t.pencolor((r, g, b))

        # Move the turtle to the correct position
        t.setpos(x, y)

        # Draw a pixel at the current position
        t.dot()

# Wait for the user to close the window
turtle.exitonclick()