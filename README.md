# circuitpython_stuff
A repo to store test programs, examples, etc. as I'm tinkering with CircuitPython

## displayio make_transparent()/make_opaque() demo test trans_opaq_test.py
I ran into some issues trying to switch between transparent and colored fills for
some buttons I was using in a program.  After chasing some code around, I think that
the make_transparent() and make_opaque() functions in displayio do not work after the initial 
creation of the shape object.

That is, once a shape (the base for a button, as well) is created with either fill=<some color>
or fill=None the shape will act as a filled OR transparent shape from then on. 

It seems like the intent of those functions is to allow the status to change, but it doesn't work. 
Which, in turn, means that the fill and outline setters in Adafruit_CircuitPython_Display_Shapes 
cannot toggle from filled to transparent, either.  The code structure implies that was the intent,
but I don't think that it works.

The trans_opaq_test.py file implements a simple demo/test that shows the failure.  By selecting
whether or not the starting fill is a color or None (transparent), the related failure can be seen.

If the starting shape starts with a color, the program will cycle through a few different colors 
and then attempt to make the shape transparent which will not work.

If the starting shape is transparent (fill=None), the program will again cycle through different colors
which will have NO effect as expected, but then it will attempt to change the body color to an actual
fill color.  This should work, but doesn't.

I believe the bug itself is buried somewhere in the displayio core module.  But I don't fully understand 
how the core all stitches together or works at this point.  

*NOTE:*  make_opaque() is never explicitly called from roundrect, but make_transparent() is. I don't know make_opaque()
is called somewhere under the covers of the displayio stuff, yet.

Maybe someone with more experience can have a look?
