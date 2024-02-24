from psd_tools import PSDImage
from PIL import Image
from time import sleep
from tqdm import tqdm
# from colorama import Fore, Back, Style


psd_name = "walk"
psd = PSDImage.open(psd_name + '.psd')
frames = []
length = len(psd._layers)
print(f" starting program. \n Converting {length} layers to imgs...\n") 
sleep(1)
for layer in tqdm(psd):
    image = layer.composite(viewport=None, force=False, color=1.0, alpha=0.0, layer_filter=None, apply_icc=False)
    frames.append(image)
print(f'...\n')

widths, heights = zip(*(i.size for i in frames)) 
total_width = sum(widths) #horizontal max
max_height = max(heights) #height of largest os the base

spritesheet = Image.new('RGB', (total_width, max_height))

x_offset = 0
print(f'rendering spritesheet! ....\n')
for im in  tqdm(frames):
  sleep(.07)
  spritesheet.paste(im, (x_offset,0))
  x_offset += im.size[0]

spritesheet.save(f'{psd_name}.png')

print("\ndone!")


