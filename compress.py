from PIL import Image
import os
import json
from menu import menu
from concurrent.futures import ThreadPoolExecutor
import time

def validate_options(redimention, resolution, convert):
    redimention_map = {1: 0, 2: 5, 3: 10, 4: 15, 5: 20, 6: 25, 7: 30, 8: 35, 9: 40, 10: 45, 11: 50}
    resolution_map = {1: 60, 2: 70, 3: 80, 4: 90, 5: 100}
    convert_map = {1: 1, 2: 2}
    
    if redimention not in redimention_map or resolution not in resolution_map or convert not in convert_map:
        raise ValueError("Invalid option selected")
        
    return redimention_map[redimention], resolution_map[resolution], convert_map[convert]

def create_folder(path):

    if not os.path.isdir(path):
        print('Not found folder, creating file <Saved Pictures Compresseds>')
        os.mkdir(path)

def redimension_cal(im1, redimention):
    width, height = im1.size
    width: int = int(width - (width * redimention / 100))
    height: int = int(height - (height * redimention / 100))
    return width, height

def redimension(im1, redimention):
    im1.thumbnail(redimension_cal(im1, redimention), Image.Resampling.LANCZOS)
    return im1

def metadata(im1):
    img_no_metadata = Image.new(im1.mode, im1.size)
    img_no_metadata.putdata(list(im1.getdata()))
    return img_no_metadata

def compress_save_image(im1, convert:int, namefile, ext, path, resolution):
    if convert == 1:
        if im1.mode in ("RGBA", "P"):
            im1 = im1.convert("RGB")
        namefile = namefile.replace(ext, '.jpeg')
    # resolution
    im1.save(path + '/' + namefile,format="JPEG", optimize=True, quality=resolution)

def process_image(namefile, redimention, resolution, convert, path, extension):
    try:
        # list files
        name, ext = os.path.splitext('./' + namefile)

        # Check if the file is an image
        if ext.lower() in extension['commonNonImageExtensions']:
            return

        if ext.lower() in extension['commonImageExtensions']:
            im1 = Image.open('./' + namefile)
                
            # Redimention
            im1 = redimension(im1, redimention)
                
            # Remove metadata
            im1 = metadata(im1)
                
            # convert
            compress_save_image(im1, convert, namefile, ext, path, resolution)

    except Exception as e:
        print(f"Error processing {namefile}: {e}")
        
def compress_parallel():
    try:
        
        # validate options
        redimention, resolution, convert = validate_options(*menu())
        
        #Tiempo inicial
        inicio = time.time()
        
        path = os.path.join('.', 'Compressed Photos')

        # Create folder
        create_folder(path)
            
        # Open valid extensions
        with open('extensions.json', 'r') as file:
            extension = json.load(file)
        
        with ThreadPoolExecutor() as executor:
            for namefile in os.listdir('./'):
                executor.submit(process_image, namefile, redimention, resolution, convert, path, extension)
                
        print('Compressed Photos Complete')
        fin = time.time()
        print(f"El programa tomó {fin - inicio} segundos en ejecutarse.")
        
    except Exception as e:
        print(f"Error: {e}")
        print('Compressed Photos Complete')