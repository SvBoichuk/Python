from PIL import Image

jpgImage = Image.open("world.jpg")

#area = (100,100, 300, 375)

print(jpgImage.size)
print(jpgImage.format)

#cropped_img = jpgImage.crop(area)
#cropped_img.save('new.jpg')

picture_size = jpgImage.size
print("size: ", picture_size)

color_mode = jpgImage.mode
print("color mode = ", color_mode)

red, green, blue = jpgImage.split()

newImage = Image.merge("RGB", (green, blue, red))
newImage.show()

transponseImage = jpgImage.transpose(Image.FLIP_LEFT_RIGHT)
transponseImage.show()

#jpgImage.show();

