"""
I ran into some issues trying to switch between transparent and colored fills for some buttons I was using in a program.
After chasing some code around, I think that the make_transparent() and make_opaque() functions in displayio do not work
after the initial creation of the shape object.

That is, once a shape (the base for a button, as well) is created with either fill= or fill=None the shape will act as a
filled OR transparent shape from then on.

It seems like the intent of those functions is to allow the status to change, but it doesn't work. Which, in turn, means
that the fill and outline setters in Adafruit_CircuitPython_Display_Shapes cannot toggle from filled to transparent,
either. The code structure implies that was the intent, but I don't think that it works.

The trans_opaq_test.py file implements a simple demo/test that shows the failure. By selecting whether or not the
starting fill is a color or None (transparent), the related failure can be seen.

If the starting shape starts with a color, the program will cycle through a few different colors and then attempt to
make the shape transparent which will not work.

If the starting shape is transparent (fill=None), the program will again cycle through different colors which will have
NO effect as expected, but then it will attempt to change the body color to an actual fill color.
This should work, but doesn't.

I believe the bug itself is buried somewhere in the displayio core module. But I don't fully understand how the core
all stitches together or works at this point.

Maybe someone with more experience can have a look?


"""

import time
from adafruit_pyportal import PyPortal
from adafruit_display_shapes.roundrect import RoundRect

# Some colors
WHITE = 0xffffff
BLUE = 0x094A85
LIGHT_BLUE = 0x13BDF9
DARK_BLUE = 0x0D2035
LIGHT_GREEN = 0x009A6E
GREEN = 0x45E83A
ORANGE = 0xDF550F
RED = 0xDB1308
GREY = 0x3B3C3E
BLACK = 0x000000

# This will control how the initial shape is created.
# fill = True  -> fill=WHITE
# fill = False -> fill=None
fill = False

# Initialize PyPortal with black background
pyportal = PyPortal(default_bg=BLACK)

# Add a square
if fill is True:
    roundrect = RoundRect(100, 60, 120, 120, 10, fill=WHITE, outline=WHITE, stroke=5)
else:
    roundrect = RoundRect(100, 60, 120, 120, 10, fill=None, outline=WHITE, stroke=5)

pyportal.splash.append(roundrect)
time.sleep(2.0)

# Cycle through a few colors then try a test case
# Test will yield different results based on value of the fill variable

while True:

    # If the square was initially created with a color fill,
    # cycle through green, light blue, orange, and red
    # the body of the square should change colors every 2 seconds

    # However, if the shape was initially created with fill=None,
    # the body will be transparent, and these color changes should have no effect

    roundrect.fill = GREEN
    time.sleep(2.0)

    roundrect.fill = LIGHT_BLUE
    time.sleep(2.0)

    roundrect.fill = ORANGE
    time.sleep(2.0)

    roundrect.fill = RED
    time.sleep(2.0)

    # Now, time to break it...

    # If the shape was initially created with a color fill,
    # try making it transparent
    # I would expect this to make the last color fill (red) disappear and
    # the black background color will be visible. But that doesn't happen
    # and the red remains visible
    if fill is True:
        roundrect.fill = None

    # If the shape was created with fill=None, try changing it to blue
    # I would expect this to add blue color back to the body of the shape
    # But the shape remains transparent
    else:
        roundrect.fill = BLUE

    time.sleep(2.0)
