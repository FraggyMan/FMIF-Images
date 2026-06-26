"""A converter and deconverter for my own .FMIF image format. This can be used as a module, or as a command line tool.\n
Created by FraggyMan.
---------------------
"""
import PIL.Image as image
from json import load, dump, loads, dumps
import numpy as np
from zlib import decompress, compress
import sys

__author__ = "FraggyMan"
__version__ = "1.0.0.0"

def convertToFMIF(fp: str, output: str) -> None:
    """Converts any image file to a .FMIF file.

    Args:
        fp (str): The input file path.
        output (str): The output file path.
    """
    imageFile = image.open(fp)
    loadedImage = imageFile.load()
    imageSize = imageFile.size
    imageHeight = imageSize[1]
    imageWidth = imageSize[0]
    imageData = []
    row = []

    for x in range(imageHeight):
        for y in range(imageWidth):
            row.append(list(loadedImage[y,x]))
        imageData.append(row)
        row = []
    
    imageData = str(imageData)
    imageData = imageData.replace(" ", "")
    converted = {
        "res":[imageWidth, imageHeight],
        "data":imageData
    }
    with open(output, "wb+") as f:
        compressedImage = compress(bytes(dumps(converted), encoding="utf-8"))
        f.write(compressedImage)

    imageFile.close()

def convertFromFMIF(fp: str, output: str) -> None:
    """Converts a .FMIF to any image file.

    Args:
        fp (str): The input file path.
        output (str): The output file path.
    """
    with open(fp, "rb") as f:
        decompressedImage = decompress(f.read())
        fmifImage = loads(decompressedImage)
    imageHeight = fmifImage["res"][1]
    imageWidth = fmifImage["res"][0]
    imagePixels = loads(fmifImage["data"])
    imagePixels = np.array(imagePixels, dtype=np.uint8)
    loadedOutput = open(output, "w+")
    loadedOutput.close()
    loadedOutput = image.frombytes("RGB", (imageWidth, imageHeight), imagePixels)
    loadedOutput.save(output)

def help() -> None:
    """Prints the help for the FMIF command.
    """
    print("Help:\n\nSyntax:\nFMIF.py [-t/-f] [input file] [output file]\n\nSwitches:\nt: Convert input to FMIF format.\nf: Convert input from FMIF format.")

if len(sys.argv) == 1:
    pass
else:    
    if ("-t" in sys.argv) ^ ("-f" in sys.argv):
        if "-t" in sys.argv:
            sys.argv.remove("-t")
            convertToFMIF(sys.argv[1], sys.argv[2])
        else:
            sys.argv.remove("-f")
            convertFromFMIF(sys.argv[1], sys.argv[2])
    elif "-?" in sys.argv:
        help()