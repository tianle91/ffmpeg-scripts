from glob import glob
from pathlib import Path
import os

vf_argument = 'transpose=1'
suffix = '(rotcw_90)'
included_extensions = ['mp4', 'mkv']
output_folder = 'output'

os.makedirs(output_folder, exist_ok=True)

l = sorted([
    *glob(f'*.{ext}')
    for ext in included_extensions
])

for i, p in enumerate(l):
    p_suffix = Path(p).suffix
    if p_suffix not in excluded_extensions:
        output_path = os.path.join(output_folder, Path(p).stem + f' {suffix}' + p_suffix)
        print(f'[{i} / {len(l)}] Processing: {p} --> {output_path}')
        os.system(f'ffmpeg -hwaccel cuda -i "{p}" -vf "{vf_argument}" "{output_path}"')
