from glob import glob
from pathlib import Path
import os

l = glob('*')
for p in l:
    output_path = Path(p).stem + ' (rotccw_90)' + Path(p).suffix
    print(f'Rotating counter-clockwise 90: {p} -> {output_path}')
    os.system(f'ffmpeg -i {p} -vf "transpose=2" {output_path}')
