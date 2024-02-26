


import os
from psd_tools import PSDImage
from PIL import Image
import sys
from bcolors import bc
import glob
import inquirer
from pprint import pprint
from tqdm import tqdm
sys.path.append(os.path.realpath("."))

print(f" Welcome to the sprite sheet combiner! This programs allows to to combine single animations like the ones generated from {bc.B} psd_to_spritesheet.py{bc.E} into a single vertical sprite sheet with multiple animations (PNG format)\n ")
print(f"Make sure to move the sheets you want to combine into the spriteSheets directory ")

pngs = []
output_sheet=None
height=0
maxWidth=0
name="example"
names = []

def createNewSheet():
    widths, heights = zip(*(i.size for i in pngs)) 
    height= sum(heights) #horizontal max
    maxWidth = max(widths) 
    output_sheet = Image.new('RGB', (maxWidth, height))
    y_offset = 0
    for img in tqdm(pngs,colour="green",postfix="psd-to-spritesheet",dynamic_ncols=True, desc="frames to spritesheet "):
        output_sheet.paste(img, (0,y_offset))
        y_offset += img.size[1]
        output_sheet.save(f'./combinedSpritesheets/example.png', )
   

#Pngs
dir_path = "./spritesheets"
for filepath in glob.glob(f"{dir_path}/*.png"):
    #array of name: (regex) path: path, imgWidth
    o=Image.open(filepath)
    maxWidth = o.size[0] if o.size[0] > maxWidth else print()
    height += o.size[1]
    pngs.append(o)
    names.append(filepath)



# eh =list(map((lambda x: x.name), getAllPNGs()))
print(f"Which of these do you wish to combine? \n [ARROW KEYS + SPACEBAR to select]/n/n")
answers = inquirer.prompt([
    inquirer.Checkbox(
        "spritesheets",
        message="select 2 or more",
        choices=names,
        default=pngs  
    ),  
])


createNewSheet()



