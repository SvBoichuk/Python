from PIL import Image

jpgImage = Image.open("world.jpg")

area = (100,100, 300, 375)

print(jpgImage.size)
print(jpgImage.format)

cropped_img = jpgImage.crop(area)

cropped_img.save('new.jpg')

jpgImage.show();

