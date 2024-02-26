from psd_tools import PSDImage
from PIL import Image
from time import sleep
from tqdm import tqdm
from bcolors import bc

psd_name = "talk"
psd = PSDImage.open('./psds/' +psd_name + '.psd')
frames = []
length = len(psd._layers)

print( f"{bc.b}Looking for{bc.E} {bc.g} {psd_name}.psd {bc.E} \n ") 
print( f"{bc.y} WARNING: Make sure your psd is inside the psd folder... {bc.E} \n ")  
print( f"{bc.y}WARNING: Make sure all layers are not in GROUPS{bc.E}\n")

print( f"🎨{bc.b}Converting {length} layers...{bc.E}🖼️\n")
sleep(1)

for layer in tqdm(psd, colour="green", postfix="psd-to-spritesheet", dynamic_ncols=True, desc="layers to frames",):
     #switch to visible
    image = layer.composite(viewport=None, force=False, color=1.0, alpha=0.0, layer_filter=None, apply_icc=False)
    image.visible = True
    frames.append(image)

widths, heights = zip(*(i.size for i in frames)) 
total_width = sum(widths) #horizontal max
max_height = max(heights) #height of largest os the base
spritesheet = Image.new('RGB', (total_width, max_height))
print(f'{bc.b}rendering spritesheet! ....\n {bc.E}')

x_offset = 0
for frame in  tqdm(frames,colour="green",postfix="psd-to-spritesheet",dynamic_ncols=True, desc="frames to spritesheet "):
  sleep(.07)
  spritesheet.paste(frame, (x_offset,0))
  x_offset += frame.size[0]

spritesheet.save(f'./spritesheets/{psd_name}.png')
print(f'{bc.b}spritesheet saved as {psd_name}.png \n {bc.E}')
print(f"{bc.g}\n done! Converted {length} layers successfully {bc.E}")
