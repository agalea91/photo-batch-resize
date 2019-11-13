# -*- coding: utf-8 -*-
__author__ = 'Alex Galea'

# Usage e.g.
# python photo-batch-resize-constrained.py --images-folder=lightroom-exports --max-px-size=1080

EXTENSIONS = [
    'jpg', 'jpeg', 'png',
    'JPG', 'JPEG', 'PNG',
]

import click
import glob
import os
from PIL import Image

@click.command()
@click.option(
    '--max-px-size',
    default=2560,
    help='The max height / width of image in pixels.'
)
@click.option(
    '--images-folder',
    default='images',
    help='Name of folder containing images.'
)
def main(max_px_size, images_folder):
    imgs = []
    for ext in EXTENSIONS:
        imgs += sorted(glob.glob(os.path.join(images_folder, '*.{}'.format(ext))))
    print('Image files to resize:')
    print('\n'.join(imgs))
    output_folder = '{}-{}px'.format(images_folder, max_px_size)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for img_path in imgs:
        try:
            resize(img_path, max_px_size, output_folder)
        except Exception as e:
            with open('error.txt', 'w') as f:
                f.write(str(e))

def resize(img_path, max_px_size, output_folder):
    with Image.open(img_path) as img:
        width_0, height_0 = img.size
        out_f_name = os.path.split(img_path)[-1]
        out_f_path = os.path.join(output_folder, out_f_name)

        if max((width_0, height_0)) <= max_px_size:
            print('writing {} to disk (no change from original)'.format(out_f_path))
            img.save(out_f_path)
            return

        if width_0 > height_0:
            wpercent = max_px_size / float(width_0)
            hsize = int(float(height_0) * float(wpercent))
            img = img.resize((max_px_size, hsize), Image.ANTIALIAS)
            print('writing {} to disk'.format(out_f_path))
            img.save(out_f_path)
            return
            
        if width_0 < height_0:
            hpercent = max_px_size / float(height_0)
            wsize = int(float(width_0) * float(hpercent))
            img = img.resize((wsize, max_px_size), Image.ANTIALIAS)
            print('writing {} to disk'.format(out_f_path))
            img.save(out_f_path)
            return

if __name__ == '__main__':
    main()
