"""A viewer for my .FMIF image format. You can either use the command line, or drag and drop the .FMIF file onto the script and it will view the file.
"""
import PIL.Image as image
from FMIF import convertFromFMIF
from os.path import abspath, dirname, basename
from os import remove
import sys

def viewImage(fp: str) -> None:
    convertFromFMIF(fp=fp, output=f"{dirname(abspath(__file__))}/temp/{basename(fp)}.jpg")
    openFile = image.open(f"{dirname(abspath(__file__))}/temp/{basename(fp)}.jpg")
    openFile.show()
    openFile.close()
    remove(f"{dirname(abspath(__file__))}/temp/{basename(fp)}.jpg")

if len(sys.argv) == 1:
    pass
else:
    viewImage(sys.argv[1])