# Alphabet Tile Blocks

# Goals

Create a tool that allows users to take an image of a tile, and a text file of what to put on the tile, and create a set of output files that are the text from the file centered on the tile. Maybe allow for some effects such as font, and such. 


# Screen shot

<pre>
+-------------------------------------------------------------------+
|                                                                   |
|  [___________________] [Choose Text ] +-------------------------+ |
|                                       +-------------------------+ |
|  [___________________] [Choose Image] +-----Image---------------+ |
|                                       +-------------------------+ |
|                                       +-------Preview-----------+ |
|                                       +-------------------------+ |
|                                       +-------------------------+ |
|                                       +-------------------------+ |
|                                                                   |
| [Quit]                                                    [Start] |
+-------------------------------------------------------------------+
</pre>

You can choose a text file, and choose an image of the tile. Then the
image of the tile will be shown on the right in the Image Preview box.

Then you can click start, and it will then generate however many tiles,
one for each text line in the text file.

So if the input file was

<pre>
A
B
C
</pre>

It would create 3 tiles, one for 'A', 'B', and 'C'.