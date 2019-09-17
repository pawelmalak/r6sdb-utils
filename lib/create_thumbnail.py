import os
from PIL import Image

def create_thumbnail(image_input_path, image_output_path):

  # open image
  image = Image.open(image_input_path)

  # crop user avatar
  image.thumbnail((605, 340), Image.ANTIALIAS)

  # save image
  image.save(image_output_path)