from psd_tools import PSDImage
from PIL import Image
from time import sleep
from tqdm import tqdm

class bcolors:
    CYAN = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

psd_name = "walk"
psd = PSDImage.open(psd_name + '.psd')
frames = []
length = len(psd._layers)
print( f"{bcolors.CYAN}Looking for{bcolors.ENDC} {bcolors.GREEN} {psd_name}.psd {bcolors.ENDC} \n ")  
print( f"🎨{bcolors.BOLD}Converting {length} layers...{bcolors.ENDC}🖼️\n")
sleep(1)

for layer in tqdm(psd, colour="green", postfix="psd-to-spritesheet", dynamic_ncols=True, desc="layers to frames",):
    image = layer.composite(viewport=None, force=False, color=1.0, alpha=0.0, layer_filter=None, apply_icc=False)
    frames.append(image)

widths, heights = zip(*(i.size for i in frames)) 
total_width = sum(widths) #horizontal max
max_height = max(heights) #height of largest os the base
spritesheet = Image.new('RGB', (total_width, max_height))
print(f'{bcolors.CYAN}rendering spritesheet! ....\n {bcolors.ENDC}')

x_offset = 0
for frame in  tqdm(frames,colour="green",postfix="psd-to-spritesheet",dynamic_ncols=True, desc="frames to spritesheet "):
#   sleep(.07)
  spritesheet.paste(frame, (x_offset,0))
  x_offset += frame.size[0]

spritesheet.save(f'{psd_name}.png')
print(f'{bcolors.CYAN}spritesheet saved as {psd_name}.png \n {bcolors.ENDC}')

print(f"{bcolors.GREEN}\n done!{bcolors.ENDC}")
