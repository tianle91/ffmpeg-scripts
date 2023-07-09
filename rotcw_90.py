# rotate 90
from glob import glob
from pathlib import Path
import os

l = glob('*')
for p in l:
    output_path = Path(p).stem + ' (rotcw_90)' + Path(p).suffix
    print(f'Rotating 90: {p} -> {output_path}')
    os.system(f'ffmpeg -i {p} -vf "transpose=1" {output_path}')
