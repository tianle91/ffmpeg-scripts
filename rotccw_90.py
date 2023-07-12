from glob import glob
from pathlib import Path
import os

excluded_extensions = ['.py',]
l = glob('*')
for p in l:
    if Path(p).suffix in excluded_extensions:
        continue
    else:
        output_path = Path(p).stem + '_(rotccw_90)' + Path(p).suffix
        print(f'Rotating counter-clockwise 90: {p} -> {output_path}')
        os.system(f'ffmpeg -i "{p}" -vf "transpose=2" "{output_path}"')
