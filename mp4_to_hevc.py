from glob import glob
from pathlib import Path
import os

l = glob(f'*.mp4')
for p in l:
    output_path = Path(p).stem + '_hevc.mp4'
    print(f'Converting to mp4: {p} -> {output_path}')
    os.system(f'ffmpeg -y -i {p} -c:v libx265 {output_path}')