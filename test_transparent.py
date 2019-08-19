"""
test_transparent.py

A simple test to demonstrate the behavior of a RoundRect when initializing
as a transparent shape using fill=None.

Also uses my_roundrect.py which is a slightly modified version of
Adafruit_CircuitPython_Display_Shapes that includes an explicit call
to palette.make_opaque() in the fill color setter function.

"""

import time
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text.label import Label
from adafruit_pyportal import PyPortal
# from adafruit_display_shapes.roundrect import RoundRect
from my_roundrect import RoundRect

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

# Load the font to be used on the buttons
font = bitmap_font.load_font("/fonts/Dina.bdf")

# Initialize PyPortal with black background
pyportal = PyPortal(default_bg=BLACK)

roundrect = RoundRect(100, 60, 120, 120, 10, fill=None, outline=WHITE, stroke=5)

pyportal.splash.append(roundrect)
time.sleep(2.0)

# These should fill with a color
roundrect.fill = GREEN
time.sleep(2.0)

roundrect.fill = LIGHT_BLUE
time.sleep(2.0)

roundrect.fill = ORANGE
time.sleep(2.0)

roundrect.fill = RED
time.sleep(2.0)

while True:
    pass