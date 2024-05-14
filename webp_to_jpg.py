from PIL import Image
from glob import glob

for p in glob('*.webp'):
    p_out = p.replace('.webp', '.jpg')
    print(f'Converting {p} to {p_out}')
    Image.open(p).save(p_out)
