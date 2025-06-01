from PIL import Image
from PIL import ImageFile
from PIL import ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw 

def open_image() -> ImageFile:
    while True:
        path = input("Enter path to image: ")
        try:
            im = Image.open(path)
            break
        except OSError as e:
            if "broken data stream" in str(e) or "truncated" in str(e):
                print("Error: Encountered problem when reading/analyzing file.")
            else:
                print("Error: Encountered a real PC problem.")
    return im

def help():
    print("1 - Flip image vertically")
    print("2 - Flip image horizontally")
    print("3 - Flip image along main diagonal")
    print("4 - Flip image along secondary diagonal")
    print("5 - Sepia")
    print("6 - Increase brightness")
    print("7 - Decrease brightness")
    print("8 - Average color")
    print("9 - Add text")

def run(image: ImageFile) -> ImageFile:
    command = int(input("Enter command: "))
    if command == 1:
        return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    if command == 2:
        return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if command == 3:
        return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM).transpose(Image.Transpose.ROTATE_270)
    if command == 4:
        return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM).transpose(Image.Transpose.ROTATE_90)
    if command == 5:
        width, height = image.size
        pixelData = image.load()
        for x in range(width):
            for y in range(height):
                r = pixelData[x, y][0]
                g = pixelData[x, y][1]
                b = pixelData[x, y][2]
                pixel = (int(r * 0.393 + g * 0.769 + b * 0.189),
                         int(r * 0.349 + g * 0.686 + b * 0.168),
                         int(r * 0.272 + g * 0.534 + b * 0.131))
                image.putpixel((x, y), pixel)
        return image
    if command == 6:
        enhancer = ImageEnhance.Brightness(image)
        factor = float(input("Enter k: "))
        return enhancer.enhance(1 + factor)
    if command == 7:
        enhancer = ImageEnhance.Brightness(image)
        factor = float(input("Enter k: "))
        return enhancer.enhance(1 - factor)
    if command == 8:
        width, height = image.size
        pixelData = image.load()
        r = g = b = 0
        for x in range(width):
            for y in range(height):
                r += pixelData[x, y][0]
                g += pixelData[x, y][1]
                b += pixelData[x, y][2]
        r /= width * height
        g /= width * height
        b /= width * height
        for x in range(width):
            for y in range(height):
                pixel = (int(r), int(g), int(b))
                image.putpixel((x, y), pixel)
        return image
    if command == 9:
        draw = ImageDraw.Draw(image)
        try:
            x = int(input("x: ")) 
            y = int(input("y: "))
            draw.text((x, y), "Text", (255, 255, 255))
        except TypeError as e:
            print(e)
        return image
    if command == 10:
        draw = ImageDraw.Draw(image)
        try:
            x1 = int(input("x1: "))
            y1 = int(input("y1: "))
            x2 = int(input("x2: "))
            y2 = int(input("y2: "))
            draw.rectangle([(x1, y1), (x2, y2)], (255, 0, 0))
        except TypeError as e:
            print(e)
        return image

image = open_image()
help()
image = run(image)
image.show()