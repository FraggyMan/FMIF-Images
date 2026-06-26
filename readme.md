# FMIF (FraggyMan Image Format)
FMIF is an image format that I created for fun and to explore the possibilities for file format design. It is a command line tool to convert and convert back to images.

# Disclaimer
FMIF is still somewhat in development and changes may be present.

# Dependencies
To run FMIF and FMIFView, you need these modules:
<ul>
    <li>Pillow</li>
    <li>Numpy</li>
</ul>
If you don't have these modules, you must install them using PIP.<br>
<br>

# How to use command line tool
The command is simply called FMIF.py.<br>
<br>
For help, type "fmif.py -?"
<h2>Here is the syntax for the command</h2>
<code>fmif.py [-t/-f] [input file] [output file]</code>
<h2>Switches</h2>
<ul>
    <li>t: Converts the input image to an output FMIF file.</li>
    <li>f: Converts the FMIF file input to an image output.</li>
</ul>
<h2>Arguments</h2>
<ul>
    <li>input file: Is the file to operate on.</li>
    <li>output file: Is the file that will be generated as a result of the command you chose.</li>
</ul>

# What does the data actually look like?
The data is a JSON file containing the dimensions and the pixel data. That JSON file is then compressed with the DEFLATE algorithim.

# Credits
Made by @FraggyMan.