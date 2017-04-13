from PIL import Image, ImageDraw
import math

image = Image.new("RGB", (512, 512))
draw = ImageDraw.Draw(image)
# image.putpixel((256,256),(255,255,255))

# For each branch - half the branch, rotate
# Create a trunk
# Recursively call drawBranch on endpoints until the branch length
# is smaller than some number
def drawBranch(image, draw, startX, startY, length, theta):
    endY = length * math.sin(theta) + startY
    endX = length * math.cos(theta) + startX
    draw.line((startX, startY, endX, endY), fill=128)

drawBranch(image, draw, 256, 256, 50, 0)

image.show()
