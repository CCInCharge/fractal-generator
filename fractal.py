from PIL import Image, ImageDraw, ImageGrab
import math
import random

# image.putpixel((256,256),(255,255,255))

# For each branch - half the branch, rotate
# Create a trunk
# Recursively call drawBranch on endpoints until the branch length
# is smaller than some number

def randomColor():
    colors = [(0, 255, 26),
    (162, 255, 0),
    (255, 205, 0),
    (26, 0, 225),
    (255, 0, 255),
    (255, 0, 0)]
    return random.choice(colors)

def drawBranch(color, image, draw, startX, startY, length, lengthFactor,
theta, delta):
    endY = length * math.sin(theta) + startY
    endX = length * math.cos(theta) + startX
    draw.line((startX, startY, endX, endY), color)
    if (length >= 5):
        drawBranch(color, image, draw, endX, endY, length * lengthFactor,
        lengthFactor, theta + math.pi / delta, delta)
        drawBranch(color, image, draw, endX, endY, length * lengthFactor,
        lengthFactor, theta - math.pi / delta, delta)

def newRandomTree():
    screenshot = ImageGrab.grab()

    width = screenshot.size[0]
    height = screenshot.size[1]

    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    startX = width/2.0
    startY = height
    length = height/4.0
    hFactor = random.choice([1/2.0, 2/3.0])
    delta = random.choice(range(4, 13))

    drawBranch(randomColor(), image, draw, startX, startY, length, hFactor,
    3 * math.pi / 2, delta)
    image.show()

newRandomTree()
