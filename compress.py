#Only drag this archive to the photos folder and execute


from PIL import Image
import os
import json
from menu import menu

def redimension(im1, redimention):
    width, height = im1.size
    width: int = int(width - (width * redimention / 100))
    height: int = int(height - (height * redimention / 100))
    return width, height

def compress():
    redimention, resolution, convert = menu()

    try:

        redimention_map = {1: 0, 2: 5, 3: 10, 4: 15, 5: 20, 6: 25, 7: 30, 8: 35, 9: 40, 10: 45, 11: 50}
        if redimention not in redimention_map:
            raise ValueError("Invalid option selected")

        redimention = redimention_map[redimention]
        
        resolution_map = {1: 60, 2: 70, 3: 80, 4: 90, 5: 100}
        if resolution not in resolution_map:
            raise ValueError("Invalid option selected")
        
        resolution = resolution_map[resolution]

        path = os.path.join('.', 'Compressed Photos')

        if not os.path.isdir(path):
            print('Not found folder, creating file <Saved Pictures Compresseds>')
            os.mkdir(path)

        with open('extensions.json', 'r') as file:
            extension = json.load(file)

        for namefile in os.listdir('./'):
            name, ext = os.path.splitext('./' + namefile)

            if ext.lower() in extension['commonNonImageExtensions']:
                continue

            if ext.lower() in extension['commonImageExtensions']:
                im1 = Image.open('./' + namefile)
                
                im1.thumbnail(redimension(im1, redimention), Image.Resampling.LANCZOS)
                
                img_no_metadata = Image.new(im1.mode, im1.size)
                img_no_metadata.putdata(list(im1.getdata()))
                
                if convert == 1:
                    if im1.mode in ("RGBA", "P"):
                        im1 = im1.convert("RGB")
                    namefile = namefile.replace(ext, '.jpeg')
                
                im1.save(path + '/' + namefile,format="JPEG", optimize=True, quality=resolution)
        print('Compressed Photos Complete')

    except Exception as e:
        print('Error:', e)
        print('Compressed Photos Incomplete')