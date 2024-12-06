from glob import glob
from pathlib import Path
import os

l = glob(f'*.wmv')
for p in l:
    output_path = Path(p).stem + '.mp4'
    print(f'Converting to mp4: {p} -> {output_path}')
    os.system(f'ffmpeg -y -hwaccel cuda -i {p} -c:v libx264 -c:a mp3 -max_muxing_queue_size 9999 {output_path}')
