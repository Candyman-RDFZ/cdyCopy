from PIL import Image

imgpath = input()

img = Image.open(imgpath).convert('RGBA')

img.save('res.ico', format='ICO')