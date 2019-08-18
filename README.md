# circuitpython_stuff
A repo to store test programs, examples, etc. as I'm tinkering with CircuitPython

## fill_color_none_test.py

I ran into some issues trying to switch between transparent and colored fills for some buttons I was using in a recent
project.

Once a shape is created with either fill=<SOME_COLOR> or fill=None, the shape will act as either a filled **OR**
transparent shape and cannot be changed.

The issue appears to be related to the Palette core module in displayio, and the symptoms show up in
Adafruit_Display_Shapes as well as Adafruit_Display_Buttons.

It seems like the intent is to allow shapes to change from a solid color fill to transparent and vice-versa,
but it doesn't work.

This program implements a simple demo/test that shows the failure. By selecting whether or not the
starting fill is a color (solid, opaque color) or None (transparent), the related failure can be seen.

If the starting shape starts with a color, the program will cycle through a few different colors and then attempt to
make the shape transparent which will not work.

If the starting shape is transparent (fill=None), the program will again cycle through different colors which will have
NO effect as expected, but then it will attempt to change the body color to an actual fill color. This should work,
but it doe not.

I believe the bug itself is buried somewhere in the displayio core module. But I don't fully understand how the core
all stitches together or works at this point.

Maybe someone with more experience can have a look?


## trans_opaq_test.py
This test will add some lower-level explicit calls to make_transparent() and make_opaque().  However, 
they are not implemented yet.  This was the original name of fill_color_none_test.py, but I 
thought it was misleading.

Coming soon, I guess...  It's a pretty nice day out there, so I want to see the sun. :)
