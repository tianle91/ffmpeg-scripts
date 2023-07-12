from glob import glob
from pathlib import Path
import os

vf_argument = 'transpose=1'
suffix = '(rotcw_90)'
excluded_extensions = ['.py',]
os.makedirs('output', exist_ok=True)

l = glob('*')
for p in l:
    p_suffix = Path(p).suffix
    if p_suffix not in excluded_extensions:
        output_path = os.path.join('output', Path(p).stem + f' {suffix}' + p_suffix)
        os.system(f'ffmpeg -hwaccel cuda -i "{p}" -vf "{vf_argument}" "{output_path}"')

