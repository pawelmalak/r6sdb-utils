from PIL import Image, ImageFilter

# open image
image = Image.open("image.jpg")

# crop user id
cropped_image = image.crop((1396, 283, 1838, 305))

# blur user id
blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius = 10))

# paste blurred image into the original one
image.paste(blurred_image, (1396, 283, 1838, 305))

# crop user avatar
cropped_image = image.crop((1370, 60, 1431, 115))

# blur user avatar
blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius = 10))

# paste blurred image into the original one
image.paste(blurred_image, (1370, 60, 1431, 115))

# show image
image.show()