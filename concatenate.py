# concatenate abc*.mp4 into abc.mp4
from glob import glob
from pathlib import Path
import os

l = glob('*.mp4')
prefixes = sorted(list({Path(s).stem[:-1] for s in l}))
assert len(prefixes) == 1, 'Need the same prefixes:\n' + '\n'.join(prefixes)
with open('l.txt', 'w') as f:
    for s in l:
       f.write(f"file '{s}'\n")

output_fname = f"{prefixes.pop().strip().strip('-_')}.mp4"
print(f'Writing to: {output_fname}')
os.system(f'ffmpeg -f concat -safe 0 -i l.txt -c copy {output_fname}')
