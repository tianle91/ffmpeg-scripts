# concatenate abc*.mp4 into abc.mp4
from glob import glob
from pathlib import Path
import os

l = sorted(list(glob('*.mp4')))
prompt_str = (
    'Will concatenate in the following order:\n'
    + '\n'.join([f'{i:4.0f}: {s}'for i, s in enumerate(l)])
    + '\nEnter Y to proceed: '
)
if input(prompt_str).lower() == 'y':
    # find prefix
    max_i = 0
    for i in range(min([len(s) for s in l])):
        if len({s[:i] for s in l}) == 1:
            max_i = i
    # concatenate if prefix is found
    if max_i == 0:
        raise ValueError('No common prefix found!')
    else:
        prefix = l[0][:max_i]
        with open('l.txt', 'w') as f:
            for s in l:
            f.write(f"file '{s}'\n")
        output_fname = f"{prefix.strip().strip('-_')}.mp4"
        print(f'Writing to: {output_fname}')
        os.system(f'ffmpeg -f concat -safe 0 -i l.txt -c copy {output_fname}')
