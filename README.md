# PSD Spritesheet Utility

Requirements:

- Python 3

```
    from psd_tools import PSDImage
    from PIL import Image
    from time import sleep
    from tqdm import tqdm
```

## `psd_to_spritesheet.py`

Converts a multi-layered `.psd` into a horizontal spritesheet. Output is a `.png` and a `.psd` (placed in the same folder as input).

Usage:

```
python psd_to_spritesheet.py %PATH_TO_INPUT_PSD%
```

Example:

```
python psd_to_spritesheet.py ./frames/layers.psd
```
