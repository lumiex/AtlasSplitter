# AtlasSplitter
Split a sprite sheet with atlas into it's individual sprites. Useful if you happen to misplace your original resources, like I did, and need to recover them.

**Note: This version only parses libGDX based atlas files, and some properties are ignored.**

# Requirements
PIL library must be installed

# Usage
`python atlas_splitter.py atlas out_dir`

The spritesheet should be placed where it is described in the atlas file
The output files will be named with respect to the atlas data, appending a `_#` if multiple indexes exist. All sprites will be saved in PNG RGBA format.