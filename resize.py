# Python Optimize Images
# -
# - Resize images keeping aspect ratio.
# - resize.py scan the current directory and will process
# - all images (jpg, .gif, .png) and put them into "processed" folder.
# - ==========================================================================
# -   Genesis Guerrero Martinez.                                             =
# -   https://github.com/gengue (genesisdaft@gmail.com)                      =
# -   July, 2016.                                                            =
# - ==========================================================================

import os
import sys
from PIL import Image

size = 800, 500
path = '.'
newpath = 'processed'

if len(sys.argv) > 1:
    if sys.argv[1] and sys.argv[2]:
        size = int(sys.argv[1]), int(sys.argv[2])

if not os.path.exists(newpath):
    os.makedirs(newpath)

for infile in os.listdir(path):
    current = os.path.join(path, infile)

    if (os.path.isfile(current) and (infile.endswith('.jpg') or infile.endswith('.png') or  infile.endswith('.gif'))):
        print('processing "%s"' % infile)
        img = Image.open(infile)
        img.thumbnail(size, Image.ANTIALIAS)
        img.save('processed/%s' % infile, optimize=True, quality=95)
