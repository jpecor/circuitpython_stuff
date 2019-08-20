"""
test_opaque.py

A simple test to demonstrate the behavior of a RoundRect when initializing
as a shape with a solid fill color using fill=WHITE.

Also uses my_roundrect.py which is a slightly modified version of
Adafruit_CircuitPython_Display_Shapes that includes an explicit call
to palette.make_opaque() in the fill color setter function.

"""

import time
from adafruit_pyportal import PyPortal
# from adafruit_display_shapes.roundrect import RoundRect
from my_roundrect import RoundRect
from adafruit_display_text.label import Label
from adafruit_bitmap_font import bitmap_font


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

roundrect = RoundRect(100, 60, 120, 120, 10, fill=WHITE, outline=WHITE, stroke=5)
msg = Label(font, text="Exp: White", max_glyphs=15)
msg.x = 100
msg.y = 40
msg.text = "Exp: White"

pyportal.splash.append(roundrect)
pyportal.splash.append(msg)

time.sleep(2.0)

msg.text = "Exp: Green"
roundrect.fill = GREEN
time.sleep(2.0)

msg.text = "Exp: Blue"
roundrect.fill = LIGHT_BLUE
time.sleep(2.0)

msg.text = "Exp: Orange"
roundrect.fill = ORANGE
time.sleep(2.0)

msg.text = "Exp: Red"
roundrect.fill = RED
time.sleep(2.0)

# Should make the shape transparent, but does not
msg.text = "Exp: None"
roundrect.fill = None
time.sleep(2.0)

while True:
    pass