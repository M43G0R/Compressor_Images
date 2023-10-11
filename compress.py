#Only drag the archive to the photos folder and execute

from pickletools import optimize
from PIL import Image
import os
path = './Compressed Photos'

if not os.path.isdir(path):
    print('Not found, creating file <Saved Pictures Compresseds>')
    os.mkdir(path)

for namefile in os.listdir('./'):
    name, ext = os.path.splitext('./' + namefile)

    if ext in ['.png' , '.jpg', '.jpeg']:
        im1 = Image.open('./' + namefile)
        im1.save(path + '/' + namefile, optimize=True, quality=60)
print('Compressed Photos Complete')