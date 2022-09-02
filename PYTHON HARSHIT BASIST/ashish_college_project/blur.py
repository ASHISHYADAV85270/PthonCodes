from PIL import Image
import sys

image_path=sys.argv[0]
img=Image.open('tiger.jpg')

width,height=img.size
aspect_ratio =height/width
new_width=250
new_height=aspect_ratio*new_width
img=img.resize((new_width,int(new_height)))
img=img.convert('L')

pixels=img.getdata()
chars=["@","#","S","%","?","+",";",":",",","."]
new_pixels=[chars[pixels//25] for pixel in pixels]
new_pixels=''.join(new_pixels)

new_pixels_count=len(new_pixels)
ascii_image=[new_pixels[new_pixels_count: new_pixels_count +new_width]]
ascii_image="\n".join(ascii_image)
print(ascii_image)

with open("ascii_image.txt","w") as f:
    f.write(ascii_image)
    