from PIL import Image

myImage = Image.open('Sahil.jpg')

smallImage = myImage.resize((16, 16), Image.BILINEAR)

resultImage = smallImage.resize(myImage.size, Image.NEAREST)

resultImage.save('sahil.png')


