#!/usr/bin/python
import zlib
import base64
import time
from PIL import Image, ImageFile

image = open('images/image.jpg','r')
base64_image = open('images/base64_image','w')
compressed_base64_image = open('images/compressed_base64_image','w')

#generating new images
start = time.time()
base64_image_data = base64.b64encode( image.read() )
end = time.time()

print('base64 compression -> ',end - start,'seconds')

start = time.time()
compressed_base64_image_data = zlib.compress(base64_image_data)
end = time.time()
print('zlib compression -> ',end - start,'seconds')

# writing base64 files
base64_image.write( base64_image_data )
compressed_base64_image.write( compressed_base64_image_data )

#regenerating actual images
regenerated_image = open( 'images/regenerated_image.jpg','w' )
regenerated_image.write(base64.b64decode( zlib.decompress( compressed_base64_image_data) ) )

image.close()
base64_image.close()
compressed_base64_image.close()
regenerated_image.close()

img_file = Image.open('images/image.jpg');
width, height = img_file.size
try:
    img_file.save('images/regenerated_progressive_image.jpg', 
        optimize=True, 
        quality=50, 
        progressive=True
        )
except IOError:
    ImageFile.MAXBLOCK = width * height
    img_file.save('images/regenerated_progressive_image.jpg', 
              # optimize=True, 
              # quality=80, 
              progressive=True)
