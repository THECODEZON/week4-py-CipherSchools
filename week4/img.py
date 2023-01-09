#installation of pillow library
#change the image ecten
#resize imagefiles
# resize multiple images using loop
#sharpness
#brightness
#color
#contrast
#image blur, GaussianBlur

from PIL import Image, ImageEnhance

img1 = Image.open('ballon.jpg')
enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance
0 : blurry
1 : original image