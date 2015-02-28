import os
import sys
import re
from PIL import Image

xymatcher = re.compile("\s*xy: (\d+),\s*(\d+)")
sizematcher = re.compile("\s*size: (\d+),\s*(\d+)")
indexmatcher = re.compile("\s*index: ([\-\d]+)")

def write_image(name, sprites, atlas_file, out_dir):
    """Get next texture info from the atlas and write it to the
    directory"""
    rotate = atlas_file.readline() #ignore rotate
    xy = xymatcher.match(atlas_file.readline())
    x = int(xy.group(1))
    y = int(xy.group(2))
    sizes = sizematcher.match(atlas_file.readline())
    width = int(sizes.group(1))
    height = int(sizes.group(2))
    atlas_file.readline() #ignore origin
    atlas_file.readline() #ignore offset
    index_match = indexmatcher.match(atlas_file.readline())
    index = index_match.group(1)
    box = x, y, x + width, y + height
    tile = sprites.crop(box)
    name = name if index == "-1" else name + "_" + index
    out_path = os.path.join(out_dir, name + ".png")
    print "Writing sprite: ", name, " to: ", out_path, " sizes: ", width, height, x, y
    tile.save(out_path, "PNG")

def split(atlas, out_dir):
    """Open's the sheet, reads each atlas item and writes it into
    the out directory"""
    #sprites = Image.open(sheet).convert("RGBA")
    atlas_file = open(atlas)
    #read first few lines
    atlas_file.readline() #blank line
    sheet = os.path.join(os.path.dirname(atlas), atlas_file.readline().rstrip("\n"))
    sprites = Image.open(sheet).convert("RGBA") #use rgba for now
    while True:
        line = atlas_file.readline()
        if line.startswith("repeat"):
            break
    
    while True:
        name = atlas_file.readline()
        if name:
            write_image(name.rstrip("\n"), sprites, atlas_file, out_dir)
        else:
            break
    

def print_usage():
    print "Usage : python atlas_splitter.py atlas out_dir"

if sys.argv[1] == "--help":
    print_usage()
elif len(sys.argv) < 3:
    print_usage()
else:
    split(sys.argv[1], sys.argv[2])